from odoo import fields, models, api
from odoo.exceptions import UserError
import random


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
        compute="_compute_alquileres_count",
        store=True
    )

    @api.depends("vehiculos_ids.alquileres_ids")
    def _compute_alquileres_count(self):
        for record in self:
            record.alquileres_count = sum(len(vehiculo.alquileres_ids) for vehiculo in record.vehiculos_ids)

    def action_estadisticas(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Alquileres de Vehículos',
            'res_model': 'azp_alquileres_vehiculos',
            'view_mode': 'tree,form',
            'domain': [('vehiculo_id.tipo_vehiculo_id', '=', self.id)],
            'context': {'default_tipo_vehiculo_id': self.id},
        }

    def action_clasificacion_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Elegir Clasificación Energética',
            'res_model': 'azp.elegir_clasificacion_wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_tipo_vehiculo_id': self.id},
        }

    def action_generar_tipo_vehiculo(self):
        numero_azar = random.randint(1, 1000)
        nombre_tipo = f"tipo_ejemplo{numero_azar}"
        self.env.cr.execute(
            "INSERT INTO azp_tipos_vehiculos (name, clasificacion_energetica, enganche_carro) VALUES (%s, %s, %s) RETURNING id",
            (nombre_tipo, 'sin_clasificar', False)
        )
        nuevo_id = self.env.cr.fetchone()[0]

        nuevo_tipo = self.browse(nuevo_id)
        usuario = self.env.user
        compania = usuario.company_id.name
        idioma = usuario.lang

        raise UserError(
            f"Se ha creado el tipo de vehículo con éxito:\n\n"
            f"ID: {nuevo_tipo.id}\n"
            f"Nombre: {nuevo_tipo.name}\n"
            f"Enganche Carro: {'Sí' if nuevo_tipo.enganche_carro else 'No'}\n\n"
            f"Información del entorno:\n"
            f"Usuario: {usuario.name} (ID: {usuario.id})\n"
            f"Compañía: {compania}\n"
            f"Idioma: {idioma}"
        )
