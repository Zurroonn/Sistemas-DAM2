from odoo import models, fields, Command
from datetime import datetime

class InheritedInmuebles(models.Model):
    _inherit = "azp_propiedades_inmuebles"
    def action_vender_propiedad(self):
        for record in self:
            self.env["account.move"].create({
                "partner_id": record.cliente_id.id,
                "move_type": "out_invoice",
                "journal_id": 1,
                "invoice_date": fields.Date.today(),
                "invoice_line_ids": [
                    Command.create({
                        "name": "6% del precio de venta: " + str(record.precio_venta),
                        "quantity": 1,
                        "price_unit": (record.precio_venta * 0.06),
                    }),
                    Command.create({
                        "name": "Gastos de gestión (" + str(record.name) + ")",
                        "quantity": 1,
                        "price_unit": 100,
                    }),
                ]
            })
        return super().action_vender_propiedad()
