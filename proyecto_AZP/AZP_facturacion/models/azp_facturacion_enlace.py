from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class AZPAlquileresFacturacion(models.Model):
    _inherit = "azp_alquileres_vehiculos"  # Asegurar que hereda del módulo correcto

    def action_facturar_alquiler(self):
        """ Método para generar una factura al facturar un alquiler """
        for record in self:
            if record.state != 'terminado':
                raise ValidationError('El alquiler debe estar en estado "Terminado" para facturarlo.')

            # Datos de la factura
            factura_vals = {
                'partner_id': record.cliente_id.id,
                'move_type': 'out_invoice',
                'journal_id': self.env['account.journal'].search([('type', '=', 'sale')], limit=1).id,
                'invoice_date': date.today(),
                'invoice_line_ids': [
                    # Línea con información del vehículo
                    (0, 0, {
                        'name': f'{record.vehiculo_id.name} ({record.vehiculo_id.codigo}) - {record.duracion} días',
                        'quantity': 1,
                        'price_unit': record.precio_final,
                    }),
                    # Línea con los gastos del seguro obligatorio
                    (0, 0, {
                        'name': 'Gastos del seguro obligatorio',
                        'quantity': 1,
                        'price_unit': 20.0,
                    }),
                ],
            }

            # Crear la factura en el modelo `account.move`
            factura = self.env['account.move'].create(factura_vals)

            # Registrar la factura en el sistema contable
            factura.action_post()

            # Marcar el alquiler como facturado
            record.state = 'facturado'

        return {
            'name': 'Factura',
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': factura.id,
            'view_mode': 'form',
            'target': 'current'
        }
