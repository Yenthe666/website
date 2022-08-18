# -*- coding: utf-8 -*-

from odoo import fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    auto_invoice_webshop_order = fields.Boolean(
        string='Automatically invoice paid order',
        related='website_id.auto_invoice_webshop_order',
        store=True
    )

    auto_send_invoice_webshop_order = fields.Boolean(
        string='Automatically send invoices',
        related='website_id.auto_send_invoice_webshop_order',
        store=True
    )

    def cron_auto_invoice_webshop_orders(self):
        """
        Look for orders that need to be invoiced and have the automatic invoicing enabled on the related website.
        Create the invoices and send them out if setting is enabled.
        """
        sale_orders = self.env['sale.order'].search([
            ('invoice_status', '=', 'to invoice'),
            ('state', '=', 'sale'),
            ('auto_invoice_webshop_order', '=', True)
        ])
        for sale_order in sale_orders:
            if not sale_order.invoice_ids:
                invoice = sale_order._create_invoices()
                if sale_order.auto_send_invoice_webshop_order:
                    invoice.action_post()
                    mail_template = sale_order._get_sale_order_mail_template()
                    invoice.with_context(force_send=True, lang=sale_order.partner_id.lang).message_post_with_template(
                        mail_template.id, composition_mode='comment', email_layout_xmlid="mail.mail_notification_paynow"
                    )
