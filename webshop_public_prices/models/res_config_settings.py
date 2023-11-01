from odoo import fields, models


class ResConfigSettings(models.TransientModel):
	_inherit = "res.config.settings"

	webshop_hide_prices = fields.Boolean(
		string='Hide prices/Add to Cart for public users',
		related='website_id.webshop_hide_prices',
		readonly=False
	)
