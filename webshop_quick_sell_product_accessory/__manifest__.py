# -*- coding: utf-8 -*-
{
	'name': 'Website Sale Product Accessory',
	'category': 'Website',
	'version': '15.0.1.0.0',
	'author': 'Mainframe Monkey',
	'website': 'https://www.mainframemonkey.com',
	'summary': 'Website Quick Sell Product accessories',
	'description': """Website Quick Sell Product accessories""",
	'depends': [
		'sale_product_configurator',
		'website_sale',
	],
	'data': [
		'views/optional_product_view.xml',
	],
	'assets': {
		'web.assets_frontend': [
			'webshop_quick_sell_product_accessory/static/css/product_accessories.scss',
			'webshop_quick_sell_product_accessory/static/js/product_accessories.js',
		],
	},
	'license': 'LGPL-3',
}
