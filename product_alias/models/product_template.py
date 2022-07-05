from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_alias_ids = fields.Many2many(
        'product.alias',
        string='Product Aliases',
        ondelete='restrict'
    )
    product_alias_string = fields.Char(
        compute='_compute_product_alias_string',
        store=True,
        string='Alias String',
        help="Technical field used for searching purposes."
    )

    @api.depends('product_alias_ids', 'product_alias_ids.name')
    def _compute_product_alias_string(self):
        for rec in self:
            rec.product_alias_string = '\n'.join([alias.name for alias in rec.product_alias_ids])
