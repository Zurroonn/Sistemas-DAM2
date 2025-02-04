{
    'name': 'azp_alquiler_vehiculos',
    'summary': 'Módulo para la gestión del alquiler de vehículos',
    'description': 'Gestión completa de vehículos, sus tipos, características y alquileres.',
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'views/azp_vehiculos_views.xml',  # Archivo de vistas para vehículos
        'views/azp_tipos_vehiculos_views.xml',  # Archivo de vistas para tipos de vehículos
        'views/azp_caracteristicas_vehiculos_views.xml',  # Archivo de vistas para características
        'views/azp_alquileres_vehiculos_views.xml',  # Archivo de vistas para alquileres
        'views/azp_res_users_views.xml',
        'reports/azp_report_alquileres_usuarios.xml',
        'reports/azp_report_vehiculos_alquileres.xml',
        'wizards/azp_generar_matricula_wizard.xml',
        'wizards/azp_elegir_clasificacion_wizard.xml',
        'views/azp_alquiler_menu.xml',  # Archivo del menú
        'security/ir.model.access.csv',  # Archivo de permisos
    ],
    'application': True,
}
