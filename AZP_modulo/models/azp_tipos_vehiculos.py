from odoo import fields, models, api

class AzpTiposVehiculos(models.Model):
    _name = "azp_tipos_vehiculos"
    _description = "Tipos de Vehículos"
    _order = "name asc"

    name = fields.Char(string="Nombre", required=True)
    clasificacion_energetica = fields.Selection([
        ('0', '0'),
        ('eco', 'Eco'),
        ('c', 'C'),
        ('b', 'B'),
        ('sin_clasificar', 'Sin Clasificar')
    ], string="Clasificación Energética", default='sin_clasificar')
    enganche_carro = fields.Boolean(string="Enganche para Carro", default=False)
    vehiculos_ids = fields.One2many(
        comodel_name="azp_vehiculos",
        inverse_name="tipo_vehiculo_id",
        string="Vehículos Asociados"
    )
    alquileres_count = fields.Integer(
        string="Número de Alquileres",
        compute="_compute_alquileres_count"
    )

    @api.depends("vehiculos_ids")
    def _compute_alquileres_count(self):
        for record in self:
            alquileres = self.env['azp_alquileres_vehiculos'].search([('vehiculo_id.tipo_vehiculo_id', '=', record.id)])
            record.alquileres_count = len(alquileres)
