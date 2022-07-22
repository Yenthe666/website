from odoo import fields, http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleProductAccessory(WebsiteSale):
    def _prepare_product_values(self, product, category, search, **kwargs):
        values =  super(WebsiteSaleProductAccessory, self)._prepare_product_values(product, category, search, **kwargs)

        # Add order to the product values
        order = request.website.sale_get_order()
        values.update({
            'website_sale_order': order
        })

        return values

    @http.route(
        "/shop/cart/get_order_details",
        type="json",
        auth="public",
        methods=["POST"],
        website=True,
        csrf=False,
        sitemap=False,
    )
    def get_order_details(self):
        order = request.website.sale_get_order(force_create=True)
        return {'product_ids': order.order_line.product_id.ids}
