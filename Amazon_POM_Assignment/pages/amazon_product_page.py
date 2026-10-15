import re

from playwright.sync_api import Page, expect

from utils.constants import AMAZON_ADD_TO_CART


class AmazonProductPage:

    def __init__(self, page: Page):
        self.page = page

        self.add_to_cart_button = page.locator(
            AMAZON_ADD_TO_CART
        )

    def verify_product_opened(self):
        expect(
            self.page
        ).to_have_url(
            re.compile(
                r"^https://www\.amazon\.in/(?:.*/)?dp/[A-Z0-9]{10}(?:[/?].*)?$"
            )
        )

    def add_to_cart(self):
        expect(
            self.add_to_cart_button
        ).to_have_count(1)

        expect(
            self.add_to_cart_button
        ).to_be_visible()

        self.add_to_cart_button.click()