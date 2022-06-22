{
    'name': 'Real Estate',
    'application': True,
    'category': 'Marketing',
    'summary': 'Yes this is an app',
    'depends': [
        'base',
    ],
    'data': [
        'data/estate.property.type.csv',
        'security/ir.model.access.csv',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_properties_views.xml',
        'views/res_users_views.xml',
        'views/estate_menus.xml',
        "report/estate_reports.xml",
        "report/estate_report_views.xml",
    ],
    "demo": [
        "demo/estate_property_tag.xml",
        "demo/estate_properties.xml",
        "demo/estate_property_offer.xml",
    ]
}
