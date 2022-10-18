from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request, route
from odoo import http


class WebshopOrderCustomerReference(WebsiteSale):

    @http.route(['/shop/order/customer_reference'], type='http', auth='public', website=True)
    def add_customer_reference(self, **post):
        order = request.website.sale_get_order()
        ref = post.pop('client_order_ref', '')
        if ref and order:
            order.client_order_ref = ref
        return request.redirect('shop/payment')
