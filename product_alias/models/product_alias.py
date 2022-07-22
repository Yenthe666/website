from odoo import fields, models


class ProductAlias(models.Model):
    _name = "product.alias"
    _description = "Product Alias"
    _order = 'id DESC'

    name = fields.Char(
        string='Name',
        translate=True,
        required=True
    )
    active = fields.Boolean(
        default=True
    )
    product_count = fields.Integer(
        compute='_compute_product_count'
    )

    def _compute_product_count(self):
        for alias in self:
            alias.product_count = self.env["product.template"].search_count([("product_alias_ids", "=", alias.id)])

    def action_view_products(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("sale.product_template_action")
        product_template_ids = self.env["product.template"].search_read([("product_alias_ids", "=", self.id)], ['id'])
        action['domain'] = [('id', 'in', [product_template['id'] for product_template in product_template_ids])]
        return action

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "There's already an alias with this name."
                                       "You cannot create two aliases with the same name.")
    ]
