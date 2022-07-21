# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class Website(models.Model):
    _inherit = 'website'

    auto_invoice_webshop_order = fields.Boolean(
        string='Automatically invoice paid orders',
        help='Webshop orders will be automatically invoiced when they are paid immediately.'
    )

    auto_send_invoice_webshop_order = fields.Boolean(
        string='Automatically send invoices',
        help='Invoices for webshop orders will be confirmed and sent to the customer automatically.'
    )

    @api.onchange('auto_invoice_webshop_order')
    def _set_auto_send_invoice_webshop_order_false(self):
        for website in self:
            if not website.auto_invoice_webshop_order:
                website.auto_send_invoice_webshop_order = False
