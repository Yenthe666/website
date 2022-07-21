# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class Website(models.Model):
    _inherit = 'website'

    order_confirmation_mail_template_id = fields.Many2one(
        comodel_name='mail.template',
        string='Order confirmation mail template',
        domain=[('model_id.model', '=', 'sale.order')]
    )

    invoice_mail_template_id = fields.Many2one(
        comodel_name='mail.template',
        string='Invoice mail template',
        domain=[('model_id.model', '=', 'account.move')]
    )
