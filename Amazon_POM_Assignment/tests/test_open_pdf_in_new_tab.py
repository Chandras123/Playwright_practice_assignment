from playwright.sync_api import Page, expect


def test_open_pdf_in_new_tab(page: Page):
    page.goto("https://playwrightlab.github.io/")

    # Wait for the new tab while clicking Open PDF
    with page.expect_popup() as popup_info:
        page.get_by_role("button", name="Open PDF").click()

    # Get the new tab
    new_tab = popup_info.value

    # Verify the new tab opened
    expect(new_tab).to_have_url(
        lambda url: ".pdf" in url.lower()
    )

    print("Original tab:", page.url)
    print("New tab:", new_tab.url)



    # from playwright.sync_api import Page, expect


def test_open_new_tab(page: Page):
    page.goto("https://playwrightlab.github.io/")

    with page.expect_popup() as popup_info:
        page.get_by_role("button", name="Open PDF").click()

    new_tab = popup_info.value

    expect(new_tab).to_have_url(
        lambda url: ".pdf" in url.lower()
    )

    print("New tab URL:", new_tab.url)