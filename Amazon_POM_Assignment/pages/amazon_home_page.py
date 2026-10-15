from playwright.sync_api import Page

from utils.constants import (
    AMAZON_ACCOUNT,
    AMAZON_BASE_URL,
    AMAZON_CART,
    AMAZON_SEARCH_BOX,
    AMAZON_SEARCH_BUTTON,
)


class AmazonHomePage:

    def __init__(self, page: Page):
        self.page = page

        self.account_link = page.locator(AMAZON_ACCOUNT)
        self.search_box = page.locator(AMAZON_SEARCH_BOX)
        self.search_button = page.locator(AMAZON_SEARCH_BUTTON)
        self.cart = page.locator(AMAZON_CART)

    def open(self):
        self.page.goto(AMAZON_BASE_URL)

    def open_auth(self):
        self.account_link.click()

    def search_product(self, product_name: str):
        self.search_box.fill(product_name)
        self.search_button.click()

    def open_cart(self):
        self.cart.click()