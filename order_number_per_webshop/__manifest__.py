# -*- coding: utf-8 -*-
{
    'name': "Order number per webshop",

    'summary': """
        Order number sequence per webshop
    """,

    'description': """
        Order number sequence per webshop
    """,

    'author': "Mainframe Monkey",
    'website': "https://www.mainframemonkey.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['website_sale_order_configuration'],

    # always loaded
    'data': [
        'views/website_views.xml',
    ],

    "license": "LGPL-3",
}
