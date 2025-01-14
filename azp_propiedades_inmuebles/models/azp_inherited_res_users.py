from odoo import fields, models

class azp_inherited_res_users(models.Model):
    _inherit = "res.users"

    # Campo para enlazar con las propiedades asignadas al usuario
    azp_propiedades_ids = fields.One2many(
        "azp_propiedades_inmuebles",
        "agente_id",
        string="Propiedades Asignadas"
    )