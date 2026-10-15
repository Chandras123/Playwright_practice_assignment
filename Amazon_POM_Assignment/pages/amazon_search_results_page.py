from playwright.sync_api import Page, expect

from utils.constants import AMAZON_PRODUCT_RESULT


class AmazonSearchResultsPage:

    def __init__(self, page: Page):
        self.page = page

    def open_product(self, product_name: str):
        product_titles = self.page.locator(
            AMAZON_PRODUCT_RESULT.format(product_name)
        )

        # Search results are dynamically rendered.
        # Wait until at least one matching product appears.
        expect(
            product_titles
        ).not_to_have_count(
            0,
            timeout=15000
        )

        product_hrefs = product_titles.evaluate_all(
            """
            elements => [
                ...new Set(
                    elements
                        .map(element => {
                            const link = element.closest("a");
                            return link ? link.href : null;
                        })
                        .filter(Boolean)
                )
            ]
            """
        )

        assert product_hrefs, (
            f'No product link found for "{product_name}"'
        )

        self.page.goto(
            product_hrefs[0],
            wait_until="domcontentloaded"
        )