odoo.define("webshop_quick_sell_product_accessory.website_shop_product_accessory", function (require) {
    'use strict';
    var sAnimations = require('website.content.snippets.animation');
    var wSaleUtils = require('website_sale.utils');

    sAnimations.registry.ProductAccessoriesSelector = sAnimations.Class.extend({
        selector: '.product-accessories-selector',
        read_events: {
            // Detects if we click to mark a tutorial as done or as not done
            'click .product_add_suggested_product': '_onClickAddSuggestedProduct',
        },
        events: sAnimations.Class.events,
        init: function () {
            this._super.apply(this, arguments);
        },
        start: function () {
            var self = this;
        },

        _onClickAddSuggestedProduct: function (ev) {
            var self = this;
            var $main_product = $("input[name='product_id']")[0];
            var $product = $(ev.currentTarget).closest('.suggested_product');

            self._rpc({
                route: "/shop/cart/get_order_details",
            }).then(function (order) {
                // Add the main product to the cart if it isn't there yet
                if (!order['product_ids'].includes(parseInt($main_product.value))) {
                    self._rpc({
                        route: "/shop/cart/update_json",
                        params: {
                            product_id: parseInt($main_product.value),
                            add_qty: 1
                        },
                    }).then(function (data) {
                        // Update cart in navbar so that the number of products is updated
                        wSaleUtils.updateCartNavBar(data);
                        self._addAccessoryToCart(self, $product)
                    });
                } else {
                    self._addAccessoryToCart(self, $product)
                }
            });
        },

        _addAccessoryToCart: function (self, $product) {
            // Add the product to the cart
            self._rpc({
                route: "/shop/cart/update_json",
                params: {
                    product_id: $product.find('input[data-product-id]').data('product-id'),
                    add_qty: 1
                },
            }).then(function (data) {
                // Remove product from suggested products because it was already added to the cart
                $product.remove();

                // Update total suggestions, if zero, remove the suggestions part
                var total_element = $('span[id="total_suggested_products"]');
                var total = parseInt(total_element[0].textContent) - 1;
                total_element.text(total);
                if (total === 0) {
                    $('.product-accessories-selector').remove();
                }

                // Update cart in navbar so that the number of products is updated
                wSaleUtils.updateCartNavBar(data);
            });
        },
    })
});