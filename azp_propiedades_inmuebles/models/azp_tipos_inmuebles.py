from odoo import api,fields, models

class azp_tipos_inmuebles(models.Model):
    _name = "azp_tipos_inmuebles"
    _description = "Modelo (tabla) para los tipos de propiedades inmobiliarias"
    _order = "name"
    name = fields.Char('Nombre', required=True)
    inmuebles_ids = fields.One2many('azp_propiedades_inmuebles', 'tipos_id', string="Propiedades Inmuebles")
    secuencia=fields.Integer('Secuencia')

    # RESTRICCIONES
    _sql_constraints = [
        ('check_name', 'unique(name)', 'El nombre del TIPO DE PROPIEDAD debe ser único.')
    ]
