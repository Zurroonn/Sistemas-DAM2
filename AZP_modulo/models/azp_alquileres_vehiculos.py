from odoo import fields, models, api
from odoo.exceptions import ValidationError, UserError
from datetime import timedelta

class AzpAlquileresVehiculos(models.Model):
    _name = "azp_alquileres_vehiculos"
    _description = "Alquileres de Vehículos"
    _order = "state desc"  # Ordenación descendente por el campo 'state'

    vehiculo_id = fields.Many2one("azp_vehiculos", string="Vehículo", required=True)
    cliente_id = fields.Many2one("res.partner", string="Cliente", required=True)
    usuario_id = fields.Many2one("res.users", string="Usuario que Gestiona", default=lambda self: self.env.user)
    fecha_inicio = fields.Date(string="Fecha de Inicio", default=fields.Date.today, required=True)
    fecha_fin = fields.Date(string="Fecha de Fin", compute="_compute_fecha_fin", inverse="_inverse_fecha_fin", store=True)
    duracion = fields.Integer(string="Duración (días)", compute="_compute_duracion", inverse="_inverse_duracion", store=True)
    precio_final = fields.Float(string="Precio Final", compute="_compute_precio_final", store=True)
    state = fields.Selection([
        ('previo', 'Previo'),
        ('en_proceso', 'En Proceso'),
        ('terminado', 'Terminado'),
        ('facturado', 'Facturado'),
        ('cancelado', 'Cancelado')
    ], default="previo", readonly=False)

    @api.depends('fecha_inicio', 'duracion')
    def _compute_fecha_fin(self):
        for record in self:
            if record.fecha_inicio and record.duracion:
                record.fecha_fin = record.fecha_inicio + timedelta(days=record.duracion)
            else:
                record.fecha_fin = False

    def _inverse_fecha_fin(self):
        for record in self:
            if record.fecha_inicio and record.fecha_fin:
                record.duracion = (record.fecha_fin - record.fecha_inicio).days
            else:
                record.duracion = 0

    @api.depends('fecha_inicio', 'fecha_fin')
    def _compute_duracion(self):
        for record in self:
            if record.fecha_inicio and record.fecha_fin:
                record.duracion = (record.fecha_fin - record.fecha_inicio).days
            else:
                record.duracion = 0

    def _inverse_duracion(self):
        for record in self:
            if record.fecha_inicio and record.duracion:
                record.fecha_fin = record.fecha_inicio + timedelta(days=record.duracion)
            else:
                record.fecha_fin = False

    @api.depends('duracion', 'vehiculo_id.precio_diario', 'vehiculo_id.precio_semanal')
    def _compute_precio_final(self):
        for record in self:
            if record.duracion > 0:
                semanas = record.duracion // 7
                dias = record.duracion % 7
                record.precio_final = (semanas * record.vehiculo_id.precio_semanal) + (dias * record.vehiculo_id.precio_diario)
            else:
                record.precio_final = 0.0

    @api.constrains('vehiculo_id', 'cliente_id', 'usuario_id', 'fecha_inicio', 'fecha_fin')
    def _check_alquiler_constraints(self):
        for record in self:
            if not all([record.vehiculo_id, record.cliente_id, record.usuario_id, record.fecha_inicio, record.fecha_fin]):
                raise ValidationError("Todos los campos requeridos deben estar completos.")
            if record.vehiculo_id.state != 'disponible':
                raise ValidationError("El vehículo debe estar en estado disponible para alquilar.")
            overlapping = self.env['azp_alquileres_vehiculos'].search([
                ('vehiculo_id', '=', record.vehiculo_id.id),
                ('state', '!=', 'cancelado'),
                ('id', '!=', record.id),
                '|',
                ('fecha_inicio', '<=', record.fecha_fin),
                ('fecha_fin', '>=', record.fecha_inicio)
            ])
            if overlapping:
                raise ValidationError("El vehículo ya está alquilado en el periodo seleccionado.")

    def action_facturar(self):
        for record in self:
            if record.state != 'terminado':
                raise UserError("Solo se pueden facturar alquileres terminados.")

            # Verificar si existe un diario para facturas de venta
            journal = self.env['account.journal'].search([('type', '=', 'sale')], limit=1)
            if not journal:
                raise UserError("No se encontró un diario de ventas para generar la factura.")

            # Crear factura con las líneas necesarias
            factura = self.env['account.move'].create({
                'partner_id': record.cliente_id.id,
                'move_type': 'out_invoice',
                'journal_id': journal.id,
                'invoice_date': fields.Date.today(),
                'invoice_line_ids': [
                    (0, 0, {
                        'name': f"{record.vehiculo_id.name} ({record.vehiculo_id.codigo}) - {record.duracion} días",
                        'quantity': 1,
                        'price_unit': record.precio_final,
                    }),
                    (0, 0, {
                        'name': "Gastos del seguro obligatorio",
                        'quantity': 1,
                        'price_unit': 20.0,
                    }),
                ],
            })

            # Confirmar la factura
            factura.action_post()

            # Cambiar el estado del alquiler
            record.state = 'facturado'

            # Mensaje de éxito
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'account.move',
                'view_mode': 'form',
                'res_id': factura.id,
                'target': 'current',
            }

    def action_cancelar(self):
        for record in self:
            if record.state in ['previo', 'en_proceso']:
                record.state = 'cancelado'
                record.vehiculo_id.state = 'disponible'
            else:
                raise UserError("Solo se pueden cancelar alquileres en estado previo o en proceso.")

    def action_move_state_left(self):
        for record in self:
            states = ['previo', 'en_proceso', 'terminado', 'facturado', 'cancelado']
            current_index = states.index(record.state)
            if current_index > 0:
                record.state = states[current_index - 1]

    def action_move_state_right(self):
        for record in self:
            states = ['previo', 'en_proceso', 'terminado', 'facturado', 'cancelado']
            current_index = states.index(record.state)
            if current_index < len(states) - 1:
                record.state = states[current_index + 1]
