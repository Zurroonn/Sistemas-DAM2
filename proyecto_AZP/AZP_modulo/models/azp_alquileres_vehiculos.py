from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import timedelta,date


class AZPAlquileresVehiculos(models.Model):
    _name = "azp_alquileres_vehiculos"
    _description = "Alquileres de Vehículos"
    _order = "state desc"

    vehiculo_id = fields.Many2one(
        "azp_vehiculos",
        string="Vehículo",
        required=True,
        ondelete="cascade",
        domain=[('state', '=', 'disponible')]  # 🔥 Solo muestra vehículos disponibles
    )
    cliente_id = fields.Many2one(
        "res.partner",
        string="Cliente",
        required=True,
        ondelete="cascade"
    )
    usuario_id = fields.Many2one(
        "res.users",
        string="Usuario que Gestiona",
        default=lambda self: self.env.user,
        ondelete="cascade"
    )

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

    display_name = fields.Char(string="Nombre", compute="_compute_display_name", store=True)

    @api.depends('vehiculo_id', 'cliente_id', 'fecha_inicio')
    def _compute_display_name(self):
        for record in self:
            vehiculo = record.vehiculo_id.name if record.vehiculo_id else "Sin vehículo"
            cliente = record.cliente_id.name if record.cliente_id else "Sin cliente"
            fecha = record.fecha_inicio.strftime('%d/%m/%Y') if record.fecha_inicio else "Sin fecha"
            record.display_name = f"{vehiculo} - {cliente} ({fecha})"

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

    @api.depends('duracion', 'vehiculo_id')
    def _compute_precio_final(self):
        for record in self:
            if record.duracion > 0 and record.vehiculo_id:
                record.precio_final = record.duracion * (record.vehiculo_id.precio_diario or 1.0)
            else:
                record.precio_final = 0.0

    @api.constrains('vehiculo_id', 'fecha_inicio', 'fecha_fin')
    def _check_alquiler_constraints(self):
        for record in self:
            if record.vehiculo_id.state != 'disponible':
                raise ValidationError("El vehículo debe estar disponible para alquilar.")

            overlapping = self.env['azp_alquileres_vehiculos'].search([
                ('vehiculo_id', '=', record.vehiculo_id.id),
                ('state', '!=', 'cancelado'),
                ('id', '!=', record.id),
                ('fecha_inicio', '<', record.fecha_fin),
                ('fecha_fin', '>', record.fecha_inicio)
            ])
            if overlapping:
                raise ValidationError("El vehículo ya está alquilado en el periodo seleccionado.")

    def action_facturar(self):
        for record in self:
            if record.state == 'terminado':
                record.state = 'facturado'
            else:
                raise ValidationError("El alquiler solo se puede facturar si está en estado 'Terminado'.")

    def action_cancelar(self):
        for record in self:
            if record.state in ['previo', 'en_proceso']:
                record.state = 'cancelado'
                record.vehiculo_id.state = 'disponible'
            else:
                raise ValidationError("El alquiler no puede ser cancelado en este estado.")

    def action_terminar_alquiler(self):
        for record in self:
            if record.state == 'en_proceso':
                record.state = 'terminado'
                record.vehiculo_id.state = 'disponible'
                record.precio_final = record.duracion * (record.vehiculo_id.precio_diario or 1.0)
            else:
                raise ValidationError("El alquiler solo se puede terminar si está en estado 'En proceso'.")

    def action_comprobar_estado_individual(self):
        for record in self:
            if record.state in ['facturado', 'cancelado']:
                continue  # no cambia si esta facturado o cancelado
            hoy = date.today()
            if hoy < record.fecha_inicio:
                record.state = 'previo'
            elif record.fecha_inicio <= hoy <= record.fecha_fin:
                record.state = 'en_proceso'
            elif hoy > record.fecha_fin:
                record.state = 'terminado'