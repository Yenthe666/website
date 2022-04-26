# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    show_in_featured_products = fields.Boolean(
        string="Featured Products"
    )

