# -*- coding: utf-8 -*-
{
    'name': "Auto invoice webshop orders",

    'summary': """
        Automatically invoice webshop orders and email them
    """,

    'description': """
        Automatically invoice webshop orders and email them
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

        'data/ir_cron.xml',
    ],

    "license": "LGPL-3",
}
