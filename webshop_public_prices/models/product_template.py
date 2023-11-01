from odoo import models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _get_combination_info(self, combination=False, product_id=False, add_qty=1, pricelist=False, parent_combination=False, only_template=False):
        combination_info = super(ProductTemplate, self)._get_combination_info(
            combination=combination, product_id=product_id, add_qty=add_qty, pricelist=pricelist,
            parent_combination=parent_combination, only_template=only_template)
        if self.env.context.get('website_id'):
            current_website = self.env['website'].get_current_website()
            if current_website.webshop_hide_prices and self.env.user._is_public():
                combination_info.update({
                    'price_extra': 0,
                })
        return combination_info
