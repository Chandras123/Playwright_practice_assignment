from playwright.sync_api import Page, expect

from utils.constants import (
    AMAZON_CART_PRODUCT,
    AMAZON_PROCEED_TO_BUY,
)


class AmazonCartPage:

    def __init__(self, page: Page):
        self.page = page

        self.proceed_to_buy_button = page.locator(
            AMAZON_PROCEED_TO_BUY
        )

    def verify_product_in_cart(self, product_name: str):
        product = self.page.locator(
            AMAZON_CART_PRODUCT.format(product_name)
        )

        expect(
            product
        ).to_have_count(
            1,
            timeout=15000
        )

        expect(
            product
        ).to_be_visible()

    def proceed_to_buy(self):
        expect(
            self.proceed_to_buy_button
        ).to_be_visible()

        self.proceed_to_buy_button.click()