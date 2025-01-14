from odoo import fields, models, api
from odoo.exceptions import UserError,ValidationError
from datetime import timedelta, date
from odoo.tools import float_is_zero,float_compare
class azp_ofertas_inmuebles(models.Model):
    _name = "azp_ofertas_inmuebles"
    _description = "Modelo (tabla) para las ofertas de compra de propiedades inmobiliarias"
    _order="precio desc"
    precio = fields.Float(string="Precio", required=True)
    estado = fields.Selection(
        [('nueva', 'Nueva'), ('aceptada', 'Aceptada'), ('rechazada', 'Rechazada')],
        string="Estado",
        default="nueva",
        copy=False
    )
    comprador_id = fields.Many2one("res.partner", string="Comprador", required=True)
    inmueble_id = fields.Many2one("azp_propiedades_inmuebles", string="Propiedad", required=True)

    validez = fields.Integer(default=7, string="Validez (días)")
    fecha_tope = fields.Date(compute="_calcular_fecha_tope", inverse="_inverso_fecha_tope", string="Fecha Tope")
    _sql_constraints = [
        ('check_precio_esperado', 'CHECK(precio_esperado > 0)',
         'El valor del PRECIO ESPERADO debe ser estrictamente positivo.')
    ]

    # RESTRICCIONES PYTHON
    @api.constrains("precio_venta", "precio_esperado")
    def _check_precio_venta(self):
        for record in self:
            # SI EL PRECIO DE VENTA ESTÁ A CERO, NO SE COMPRUEBA LA RESTRICCIÓN
            if not float_is_zero(record.precio_venta, 2):
                # FORMULA PARA SABER SI EL PRECIO DE VENTA ES ERRONEO (NO LLEGA AL 90%)
                if float_compare(record.precio_venta, (record.precio_esperado * 0.9), 2) == -1:
                    raise ValidationError(
                        "EL PRECIO DE VENTA debe ser, al menos, del 90% del PRECIO ESPERADO. "
                        "Puede reducir el PRECIO ESPERADO para aceptar esta oferta."
                    )

    @api.depends("validez")
    def _calcular_fecha_tope(self):
        for record in self:
            if record.create_date:
                record.fecha_tope = record.create_date + timedelta(days=record.validez)
            else:
                record.fecha_tope = date.today() + timedelta(days=record.validez)

    def _inverso_fecha_tope(self):
        for record in self:
            record.validez = (record.fecha_tope - date.today()).days if record.fecha_tope else 0


    def action_aceptar_oferta(self):
        for record in self:
            if record.estado == 'aceptada':
                raise UserError("La oferta ya ha sido aceptada.")
            record.estado = 'aceptada'
            record.inmueble_id.precio_venta = record.precio
            record.inmueble_id.cliente_id = record.comprador_id
            record.inmueble_id.state = 'oferta_aceptada'

    def action_rechazar_oferta(self):
        for record in self:
            if record.estado == 'rechazada':
                raise UserError("La oferta ya ha sido rechazada.")
            record.estado = 'rechazada'



