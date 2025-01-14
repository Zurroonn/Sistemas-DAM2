from odoo import fields, models

class azpEtiquetas_inmuebles(models.Model):
    _name = "azp_etiquetas_inmuebles"
    _description = "Modelo (tabla) para las etiquetas que califican las propiedades inmobiliarias"
    _order = "name"
    name = fields.Char('Nombre', required=True)
    color=fields.Integer('Color')

    # RESTRICCIONES
    _sql_constraints = [
        ('check_name', 'unique(name)', 'El nombre del TIPO DE PROPIEDAD debe ser único.')
    ]
