{
    'name': 'Real Estate',
    'application': True,
    'category': 'Marketing',
    'summary': 'Yes this is an app',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_properties_views.xml',
        'views/estate_menus.xml',
        'views/estate_property_type_views.xml',
    ]
}