from odoo import fields, http
from odoo.http import request
from odoo.addons.website.controllers.main import Website


class WebsiteHidePrice(Website):
    @http.route()
    def autocomplete(self, search_type=None, term=None, order=None, limit=5, max_nb_chars=999, options=None):
        options = options or {}
        if request.website.webshop_hide_prices and request.env.user._is_public():
                options['displayDetail'] = False
        else:
            options['displayDetail'] = options['displayDetail']
        return super().autocomplete(search_type, term, order, limit, max_nb_chars, options)
