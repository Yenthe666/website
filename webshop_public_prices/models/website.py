from odoo import fields, models


class Website(models.Model):
	_inherit = "website"

	webshop_hide_prices = fields.Boolean(
		string='Hide prices/Add to Cart for public users',
		readonly=False
	)
