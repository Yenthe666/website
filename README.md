# Website
Apps related to Odoo it's website/webshop features:
- [webshop_public_prices](#webshop_public_prices): allow configuring to hide or show product prices and add to cart button for public users.
- [website_featured_products](#website_featured_products): allow to define which products should be featured when using the "Products" snippet.
- [product_alias](#product_alias): allow to set aliases on products so they can be found with multiple names.


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

## product_alias
Adds support to configure/add aliases on products so products can be found more easily and with multiple terms.
This support works on any search operation so by default also adds support for the Odoo webshop.
Aliases are configurable on the product itself:
![image](https://user-images.githubusercontent.com/6352350/177359218-8ed9f4ac-de66-47b1-a82c-75109f1bc9bf.png)

You can view/edit/manage all aliases from Sales > Configuration > Product Aliases:
![image](https://user-images.githubusercontent.com/6352350/177359471-fa9e6b8a-017e-4c1a-8629-d99c48d85973.png)
They are only editable, creatable and deletable by sales administrators. Normal users can only read them.
