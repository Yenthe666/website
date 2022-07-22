{
	'name': 'Product Alias',
	'category': 'Website',
	'version': '15.0.1.0',
	'author': 'Mainframe Monkey',
	'website': 'https://www.mainframemonkey.com',
	'summary': 'Product Alias',
	'description': """
	Add multiple Aliases on Product to search via Alias.
	You can use same Alias in Multiple Products.
	Search Product using assigned Alias""",
	'depends': [
		'sale_management',
	],
	'data': [
		'security/ir.model.access.csv',
		'wizards/assign_product_alias_views.xml',
		'views/product_alias_views.xml',
		'views/product_template_views.xml',
	],
	'installable': True,
	'license': 'LGPL-3',
}
