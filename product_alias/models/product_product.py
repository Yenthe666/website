from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        """ Override _search in order to grep search on product_alias_string field """
        if args:
            name = ''
            for arg in args:
                if isinstance(arg, (list, tuple)) and arg[0] == 'default_code' and isinstance(arg[2], str):
                    name = arg[2]
                    break
            if name:
                args = ['|', ('product_alias_string', 'ilike', name)] + args
        return super()._search(args, offset=offset, limit=limit, order=order, count=count, access_rights_uid=access_rights_uid)
