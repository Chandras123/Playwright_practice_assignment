from playwright.sync_api import Page


def test_multiple_tabs(page: Page):
    context = page.context

    page.goto("https://example.com")

    # Open a second tab
    second_tab = context.new_page()
    second_tab.goto("https://playwright.dev/")

    # Open a third tab
    third_tab = context.new_page()
    third_tab.goto("https://www.python.org/")

    # Get all open tabs in this context
    all_tabs = context.pages

    print("Number of tabs:", len(all_tabs))

    for index, tab in enumerate(all_tabs, start=1):
        print(f"Tab {index}: {tab.url}")

    assert len(all_tabs) == 3