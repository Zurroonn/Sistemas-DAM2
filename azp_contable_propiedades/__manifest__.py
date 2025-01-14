{
    'name': 'azp_contable_propiedades',
    'summary': 'Módulo de contabilidad para enlace de propiedades inmobiliarias',
    'description': "Con este módulo se consigue crear facturas en la venta de Propiedades Inmobiliarias",
    'license': 'LGPL-3',
    'depends': [
        'base',
        'azp_propiedades_inmuebles',
        'account'
    ],
    'data': [
        'reports/azp_inherited_propiedades_inmuebles_templates.xml',
    ],
    'application': True,
}
