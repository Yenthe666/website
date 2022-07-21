# -*- coding: utf-8 -*-
from odoo import fields, models, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    related_order_id = fields.Many2one(
        comodel_name='sale.order',
        string='Related sale order'
    )

    def action_invoice_sent(self):
        """
        Use custom mail template configured on website when using send by email wizard
        """
        account_move_send_wizard = super(AccountMove, self).action_invoice_sent()
        context = account_move_send_wizard.get('context')
        if self.related_order_id:
            template = self.related_order_id._get_sale_order_mail_template()
            if template != context.get('template'):
                context.update({
                    'default_use_template': bool(template),
                    'default_template_id': template and template.id,
                })
                account_move_send_wizard.update({
                    'context': context
                })
        return account_move_send_wizard
