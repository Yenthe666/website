# Website
Apps related to Odoo it's website/webshop features:
- [webshop_public_prices](#webshop_public_prices): allow configuring to hide or show product prices and add to cart button for public users.
- [website_featured_products](#website_featured_products): allow to define which products should be featured when using the "Products" snippet.
- [website_shop_product_accessory](#website_shop_product_accessory): allow to quick add accessories to the basket from the product (in the webshop)

## webshop_public_prices
Adds support to configure if the sale price and the 'Add to cart' button is shown on products in the shop or not.<br/>
This setting is configurable under Website > Configuration > Settings:
![image](https://user-images.githubusercontent.com/6352350/157879698-5145fbd6-9c46-4720-922a-096d834d99be.png)

When this configuration option is checked on we change the following things for public (not logged in) users:
- Hide the sales price on the /shop overview page

![image](https://user-images.githubusercontent.com/6352350/157879960-8c712ab9-303b-4519-a048-bd159d509d64.png)

- Hide the sales price on the /shop/product-xyz page
- Hide the 'Add to Cart' button on the /shop/product-xyz page and show a 'Login to see Price' button
![image](https://user-images.githubusercontent.com/6352350/157880066-7382e001-592d-4b04-ba40-27f6d0df8dc0.png)


## website_featured_products
Adds support to configure which products should be shown on the website.
This is configurable by checking the option "Featured Products" on or off on the product form:
![image](https://user-images.githubusercontent.com/6352350/165242952-f67b7520-b440-4cc5-a4d2-3d6c0fec154c.png)

The option "Featured Products" is configurable once you've dragged the building block onto the website:
![image](https://user-images.githubusercontent.com/6352350/165243133-5c499e96-2c57-4706-8344-628ab570e359.png)

## website_shop_product_accessory
Adds support for customers to quick add product accessories to the basket from the product form:
Simply install this app and for any product that has accessory products configured on the product they will be
automatically shown/selectable in the shop.
Here's what happens when the customer clicks on the "Add to cart" of the suggested accessory:
- If the product itself is already in the basket we only add the accessory,<br/
- If the product and the accessory are not in the basket we add one of each,<br/>
- If the accessory is already in the basket we no longer show it