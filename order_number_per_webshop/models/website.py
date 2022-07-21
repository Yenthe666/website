# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class Website(models.Model):
    _inherit = 'website'

    sequence_id = fields.Many2one(
        comodel_name='ir.sequence',
        domain="[('code', '=', 'sale.order')]",
        string='Sequence'
    )

    def sale_get_order(self, force_create=False, code=None, update_pricelist=False, force_pricelist=False):
        """
        Override this function so that we pass the ir.sequence configured on the website through the context
        """
        return super(
            Website, self.with_context(sequence_id=self.sequence_id)
        ).sale_get_order(force_create, code, update_pricelist, force_pricelist)
