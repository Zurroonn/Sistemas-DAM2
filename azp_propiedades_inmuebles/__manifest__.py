{
    'name': 'azp_propiedades',
    'summary': 'Módulo de gestión de propiedades inmobiliarias',
    'description': 'Propiedades Inmobiliarias',
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'views/azp_propiedades_inmuebles_views.xml',  # Archivo de vistas
        'views/azp_inmuebles_tipos_views.xml',
        'views/azp_inmuebles_etiquetas_views.xml',
        'views/azp_inmuebles_ofertas_views.xml',
        'views/azp_propiedades_menu.xml',  # Archivo del menú
        'views/azp_res_users_views.xml',
        'reports/azp_propiedades_inmuebles_reports.xml',
        'reports/azp_propiedades_inmuebles_templates.xml',
        'reports/azp_res_users_reports.xml',
        'reports/azp_res_users_templates.xml',
        'security/ir.model.access.csv',  # Archivo de permisos

    ],
    'application': True,
}
