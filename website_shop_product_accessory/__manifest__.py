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
		'sale_product_configurator', 'website_sale',
	],
	'data': [
		'views/templates.xml',
	],
	'assets': {
		'web.assets_frontend': [
			'website_shop_product_accessory/static/css/product_accessories.scss',
			'website_shop_product_accessory/static/js/product_accessories.js',
		],
	},
	'license': 'LGPL-3',
}
