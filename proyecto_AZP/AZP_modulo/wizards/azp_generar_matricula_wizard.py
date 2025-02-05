from odoo import models, fields, api
from odoo.exceptions import ValidationError

class GenerarMatriculaWizard(models.TransientModel):
    _name = 'azp.generar_matricula_wizard'
    _description = 'Asistente para generar matrícula'

    vehiculo_id = fields.Many2one('azp_vehiculos', string="Vehículo", required=True)
    numeros = fields.Char(string="Números", size=4, required=True)
    letras = fields.Char(string="Letras", size=3, required=True)

    @api.constrains('numeros', 'letras')
    def _check_matricula_format(self):
        for record in self:
            if not record.numeros.isdigit() or len(record.numeros) != 4:
                raise ValidationError("Los números de la matrícula deben tener 4 dígitos.")
            if not record.letras.isalpha() or len(record.letras) != 3:
                raise ValidationError("Las letras de la matrícula deben tener 3 caracteres alfabéticos.")

    def action_confirmar_matricula(self):
        """ Guarda la nueva matrícula en el vehículo y cierra el asistente. """
        self.vehiculo_id.matricula = f"{self.numeros}{self.letras}"
        return {'type': 'ir.actions.act_window_close'}
