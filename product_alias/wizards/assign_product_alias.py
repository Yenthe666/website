from odoo import fields, models, _


class AssignAlias(models.TransientModel):
    _name = 'assign.alias'
    _description = 'Assign Product Alias'

    action = fields.Selection([
        ('add', _('Add Aliases')),
        ('replace', _('Replace Aliases with selected ones'))],
        default='add',
        help="Select 'Add Aliases' if you want to add aliases to the existing Aliases. \n"
             "Select 'Replace' if you want to Replace all aliases with selected ones.")

    assign_product_alias_ids = fields.Many2many('product.alias',
                                                string='Select Aliases')

    def action_assign(self):
        self.ensure_one()
        products_ids = self.env[self._context.get('active_model')].browse(self._context.get('active_ids'))
        if self.action == "add":
            for each_product in products_ids:
                for each_alias in self.assign_product_alias_ids:
                    each_product.product_alias_ids = [(4, each_alias.id)]
        elif self.action == "replace":
            products_ids.product_alias_ids = [(6, 0, self.assign_product_alias_ids.ids)]
