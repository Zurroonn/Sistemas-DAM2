from odoo import fields, models

class AzpCaracteristicasVehiculos(models.Model):
    _name = "azp_caracteristicas_vehiculos"  # Nombre de la tabla en la base de datos
    _description = "Características de Vehículos"
    _order = "sequence asc"  # Ordenación por campo de secuencia

    name = fields.Char(string="Nombre", required=True)
    sequence = fields.Integer(string="Secuencia", default=10)  # Campo para gestionar la ordenación manual
