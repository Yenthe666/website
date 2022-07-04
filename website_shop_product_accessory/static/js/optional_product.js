odoo.define('website_shop_product_accessory.OptionalProductsModal', function (require) {
    "use strict";
var publicWidget = require('web.public.widget');

var ajax = require('web.ajax');
var Dialog = require('web.Dialog');
const OwlDialog = require('web.OwlDialog');
var ServicesMixin = require('web.ServicesMixin');
var VariantMixin = require('sale.VariantMixin');
var wSaleUtils = require('website_sale.utils');
require('website_sale.website_sale');
const cartHandlerMixin = wSaleUtils.cartHandlerMixin;
var OptionalProduct = publicWidget.registry.WebsiteSale.extend({

    events:  _.extend({}, {
        'click a.js_add_optional, a.js_remove': '_onAddOrRemoveOption',
    }),
    _onAddOrRemoveOption: function (ev) {
        console.log("THIS IS CALLED");
        ev.preventDefault();
        var self = this;
        var $target = $(ev.currentTarget);
        var $modal = $target.parents('.oe_advanced_configurator_modal');
        var $parent = $target.parents('.js_product:first');
        $parent.find("a.js_add, span.js_remove").toggleClass('d-none');
        $parent.find(".js_remove");

        var productTemplateId = $parent.find(".product_template_id").val();
        if ($target.hasClass('js_add')) {
            self._onAddOption($modal, $parent, productTemplateId);
        } else {
            self._onRemoveOption($modal, $parent);
        }

        self._computePriceTotal();
    },

    /**
     * @private
     * @see _onAddOrRemoveOption
     * @param {$.Element} $modal
     * @param {$.Element} $parent
     * @param {integer} productTemplateId
     */
    _onAddOption: function ($modal, $parent, productTemplateId) {
        var self = this;
        var $selectOptionsText = $modal.find('.o_select_options');

        var parentUniqueId = $parent[0].dataset.parentUniqueId;
        var $optionParent = $modal.find('tr.js_product[data-unique-id="' + parentUniqueId + '"]');

        // remove attribute values selection and update + show quantity input
        $parent.find('.td-product_name').removeAttr("colspan");
        $parent.find('.td-qty').removeClass('d-none');

        var productCustomVariantValues = self.getCustomVariantValues($parent);
        var noVariantAttributeValues = self.getNoVariantAttributeValues($parent);
        if (productCustomVariantValues || noVariantAttributeValues) {
            var $productDescription = $parent
                .find('td.td-product_name div.float-left');

            var $customAttributeValuesDescription = $('<div>', {
                class: 'custom_attribute_values_description text-muted small'
            });
            if (productCustomVariantValues.length !== 0 || noVariantAttributeValues.length !== 0) {
                $customAttributeValuesDescription.append($('<br/>'));
            }

            $.each(productCustomVariantValues, function (){
                $customAttributeValuesDescription.append($('<div>', {
                    text: this.attribute_value_name + ': ' + this.custom_value
                }));
            });

            $.each(noVariantAttributeValues, function (){
                if (this.is_custom !== 'True'){
                    $customAttributeValuesDescription.append($('<div>', {
                        text: this.attribute_name + ': ' + this.attribute_value_name
                    }));
                }
            });

            $productDescription.append($customAttributeValuesDescription);
        }

        // place it after its parent and its parent options
        var $tmpOptionParent = $optionParent;
        while ($tmpOptionParent.length) {
            $optionParent = $tmpOptionParent;
            $tmpOptionParent = $modal.find('tr.js_product.in_cart[data-parent-unique-id="' + $optionParent[0].dataset.uniqueId + '"]').last();
        }
        $optionParent.after($parent);
        $parent.addClass('in_cart');

        this.selectOrCreateProduct(
            $parent,
            $parent.find('.product_id').val(),
            productTemplateId,
            true
        ).then(function (productId) {
            $parent.find('.product_id').val(productId);

            ajax.jsonRpc(self._getUri("/sale_product_configurator/optional_product_items"), 'call', {
                'product_id': productId,
                'pricelist_id': self.pricelistId || false,
            }).then(function (addedItem) {
                var $addedItem = $(addedItem);
                $modal.find('tr:last').after($addedItem);

                self.$el.find('input[name="add_qty"]').trigger('change');
                self.triggerVariantChange($addedItem);

                // add a unique id to the new products
                var parentUniqueId = $parent[0].dataset.uniqueId;
                var parentQty = $parent.find('input[name="add_qty"]').val();
                $addedItem.filter('.js_product').each(function () {
                    var $el = $(this);
                    var uniqueId = self._getUniqueId(this);
                    this.dataset.uniqueId = uniqueId;
                    this.dataset.parentUniqueId = parentUniqueId;
                    $el.find('input[name="add_qty"]').val(parentQty);
                });

                if ($selectOptionsText.nextAll('.js_product').length === 0) {
                    // no more optional products to select -> hide the header
                    $selectOptionsText.hide();
                }
            });
        });
    },
});
return OptionalProduct;
//return OptionalProductsModal;

});
