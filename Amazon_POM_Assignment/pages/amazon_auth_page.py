from playwright.sync_api import Page, expect

from utils.constants import (
    AMAZON_AUTH_CONTINUE,
    AMAZON_AUTH_EMAIL,
)


class AmazonAuthPage:

    def __init__(self, page: Page):
        self.page = page

        self.email_input = page.locator(
            AMAZON_AUTH_EMAIL
        )

        self.continue_button = page.locator(
            AMAZON_AUTH_CONTINUE
        )

    def go_back(self):
        self.page.go_back(
            wait_until="domcontentloaded"
        )

    def enter_email_or_mobile(self, value: str):
        expect(
            self.email_input
        ).to_be_visible()

        self.email_input.fill(value)

    def click_continue(self):
        expect(
            self.continue_button
        ).to_be_visible()

        self.continue_button.click()