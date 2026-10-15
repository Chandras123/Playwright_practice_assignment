from playwright.sync_api import Page


def test_new_page_in_context(page: Page):
    context = page.context

    page.goto("https://example.com")

    with context.expect_page() as page_info:
        page.evaluate(
            "() => window.open('https://playwright.dev/', '_blank')"
        )

    new_page = page_info.value
    new_page.wait_for_load_state()

    assert "playwright.dev" in new_page.url