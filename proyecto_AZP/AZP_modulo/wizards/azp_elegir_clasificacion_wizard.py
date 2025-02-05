from odoo import models, fields, api

class ElegirClasificacionWizard(models.TransientModel):
    _name = 'azp.elegir_clasificacion_wizard'
    _description = 'Asistente para elegir clasificación energética'

    tipo_vehiculo_id = fields.Many2one('azp_tipos_vehiculos', string="Tipo de Vehículo", required=True)
    combustible = fields.Selection([
        ('electrico_bateria', 'Eléctrico de batería'),
        ('electrico_autonomia', 'Eléctrico de autonomía extendida'),
        ('electrico_hibrido', 'Eléctrico híbrido enchufable'),
        ('hibrido_no_enchufable', 'Híbrido no enchufable'),
        ('gas', 'Gas'),
        ('gasolina_2006', 'Gasolina matriculado a partir de enero de 2006'),
        ('diesel_2015', 'Diésel matriculado a partir de septiembre de 2015'),
        ('gasolina_2001_2006', 'Gasolina matriculado entre 2001 y 2006'),
        ('diesel_2006_2015', 'Diésel matriculado entre 2006 y 2015'),
        ('otros', 'Otros')
    ], string="Combustible", required=True)

    def action_confirmar_clasificacion(self):
        """ Establece automáticamente la clasificación energética basada en el combustible seleccionado. """
        clasificacion_map = {
            ('electrico_bateria', 'electrico_autonomia', 'electrico_hibrido'): '0',
            ('hibrido_no_enchufable', 'gas'): 'eco',
            ('gasolina_2006', 'diesel_2015'): 'c',
            ('gasolina_2001_2006', 'diesel_2006_2015'): 'b',
            ('otros',): 'sin_clasificar'
        }

        for key, value in clasificacion_map.items():
            if self.combustible in key:
                self.tipo_vehiculo_id.clasificacion_energetica = value
                break

        return {'type': 'ir.actions.act_window_close'}
