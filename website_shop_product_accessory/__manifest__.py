# -*- coding: utf-8 -*-
{
	'name': 'Website Sale Product Accessory',
	'category': 'Website',
	'version': '15.0.0.1.0',
	'author': 'Mainframe Monkey',
	'website': 'https://www.mainframemonkey.com',
	'summary': 'Website Sale Product Accessory',
	'description': """Website Sale Product Accessory""",
	'depends': [
		'sale_product_configurator',
	],
	'data': [
		'views/templates.xml',
	],
	'assets': {
		'web.assets_frontend': [
			'website_shop_product_accessory/static/js/optional_product.js'
		],
	},
	'license': 'LGPL-3',
}
