from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    alquileres_ids = fields.One2many(
        comodel_name="azp_alquileres_vehiculos",
        inverse_name="cliente_id",
        string="Alquileres de Vehículos"
    )
