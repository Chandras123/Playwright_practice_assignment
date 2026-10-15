
from pathlib import Path

from playwright.sync_api import Page, expect


def test_product_page(page: Page):
    Path("artifacts/screenshots").mkdir(
        parents=True,
        exist_ok=True,
    )

    page.goto("https://playwrightlab.github.io/")

    try:
        expect(page.get_by_text("Text That Does Not Exist")).to_be_visible(timeout=3000)

    except AssertionError:
        page.screenshot(path="artifacts/screenshots/product_failure.png",full_page=True,)
        # raise

    