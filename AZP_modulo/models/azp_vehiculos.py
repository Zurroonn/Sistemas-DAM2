from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta

class AzpVehiculos(models.Model):
    _name = "azp_vehiculos"  # Nombre de la tabla en la base de datos
    _description = "Gestión de Vehículos para Alquiler"
    _order = "codigo asc"  # Ordenación por defecto por el campo 'codigo'

    name = fields.Char(string="Nombre", required=True)
    codigo = fields.Char(
        string="Código",
        required=True,
        default=lambda self: f"{self.env.user.id}-{datetime.now().strftime('%d%m%Y')}"
    )
    tipo_vehiculo_id = fields.Many2one(
        "azp_tipos_vehiculos",
        string="Tipo de Vehículo",
        required=True
    )
    caracteristicas_ids = fields.Many2many(
        "azp_caracteristicas_vehiculos",
        string="Características"
    )
    alquileres_ids = fields.One2many(
        "azp_alquileres_vehiculos",
        "vehiculo_id",
        string="Alquileres"
    )
    matricula = fields.Char(string="Matrícula", required=True)
    potencia = fields.Integer(string="Potencia (CV)", default=100)
    num_plazas = fields.Integer(string="Número de Plazas", default=5)
    fecha_fabricacion = fields.Date(string="Fecha de Fabricación")
    combustible = fields.Selection([
        ('gasolina', 'Gasolina'),
        ('diesel', 'Diesel'),
        ('gas', 'Gas'),
        ('hibrido', 'Híbrido'),
        ('electrico', 'Eléctrico')
    ], string="Combustible")
    fecha_itv = fields.Date(
        string="Fecha de ITV",
        compute="_compute_fecha_itv",
        store=True
    )
    neumatico = fields.Char(string="Neumático")
    maletero = fields.Boolean(string="Maletero")
    capacidad_maletero = fields.Float(string="Capacidad del Maletero (m³)")
    precio_diario = fields.Float(string="Precio Diario", default=1.0)
    precio_semanal = fields.Float(
        string="Precio Semanal",
        compute="_compute_precio_semanal",
        store=True
    )
    numero_alquileres = fields.Integer(
        string="Número de Alquileres",
        compute="_compute_numero_alquileres",
        store=True
    )
    state = fields.Selection([
        ('disponible', 'Disponible'),
        ('alquilado', 'Alquilado'),
        ('en_reparacion', 'En Reparación')
    ], string="Estado", required=True, default='disponible', readonly=False)

    @api.depends('fecha_fabricacion')
    def _compute_fecha_itv(self):
        for record in self:
            if record.fecha_fabricacion:
                record.fecha_itv = record.fecha_fabricacion + timedelta(days=6 * 365)
            else:
                record.fecha_itv = None

    @api.depends('precio_diario')
    def _compute_precio_semanal(self):
        for record in self:
            record.precio_semanal = record.precio_diario * 5 if record.precio_diario else 0

    @api.depends('alquileres_ids')
    def _compute_numero_alquileres(self):
        for record in self:
            record.numero_alquileres = len(record.alquileres_ids)

    @api.onchange('maletero')
    def _onchange_maletero(self):
        for record in self:
            record.capacidad_maletero = 300 if record.maletero else 0

    @api.constrains('num_plazas', 'potencia', 'precio_diario')
    def _check_positive_values(self):
        for record in self:
            if any(value <= 0 for value in [record.num_plazas, record.potencia, record.precio_diario]):
                raise ValidationError("El número de plazas, la potencia y el precio diario deben ser mayores que cero.")

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'El nombre del vehículo debe ser único.'),
        ('positive_values', 'CHECK(num_plazas > 0 AND potencia > 0 AND precio_diario > 0)',
         'El número de plazas, la potencia y el precio diario deben ser mayores que cero.')
    ]

    def action_comenzar_reparacion(self):
        for record in self:
            if record.state != 'disponible':
                raise ValidationError("El vehículo debe estar en estado disponible para iniciar una reparación.")
            record.state = 'en_reparacion'

    def action_terminar_reparacion(self):
        for record in self:
            if record.state != 'en_reparacion':
                raise ValidationError("El vehículo debe estar en estado de reparación para finalizarla.")
            record.state = 'disponible'
