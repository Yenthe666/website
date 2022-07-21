# -*- coding: utf-8 -*-

from odoo import fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _find_mail_template(self, force_confirmation_template=False):
        """
        If order has a linked website, and the website is configured to use custom mail templates for orders, use that template
        """
        if self.website_id:
            if self.website_id.order_confirmation_mail_template_id \
                    and (force_confirmation_template
                         or (self.state == 'sale' and not self.env.context.get('proforma', False))):
                return self.website_id.order_confirmation_mail_template_id.id

        return super(SaleOrder, self)._find_mail_template(force_confirmation_template=force_confirmation_template)

    def _get_sale_order_mail_template(self):
        if self.website_id and self.website_id.invoice_mail_template_id:
            return self.website_id.invoice_mail_template_id
        return self.env.ref('account.email_template_edi_invoice', raise_if_not_found=False)

    def _prepare_invoice(self):
        """
        Add link to sale order on the invoice
        """
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals.update({
            'related_order_id': self.id
        })
        return invoice_vals
