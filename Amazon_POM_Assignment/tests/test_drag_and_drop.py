from playwright.sync_api import Page, expect


def test_drag_and_drop(page: Page):
    page.goto("https://playwrightlab.github.io/")

    source = page.locator("#draggable")
    target = page.locator("#droppable")

    source.drag_to(target)

    expect(target).to_contain_text("Dropped!")

def test_drag_and_drop_with_offset(page: Page):
    page.goto("https://playwrightlab.github.io/")

    source = page.locator("#draggable")
    target = page.locator("#droppable")

    source_box = source.bounding_box()
    target_box = target.bounding_box()

    assert source_box is not None
    assert target_box is not None

    page.mouse.move(
        source_box["x"] + source_box["width"] / 2,
        source_box["y"] + source_box["height"] / 2,
    )
    page.mouse.down()

    page.mouse.move(
        target_box["x"] + target_box["width"] / 2,
        target_box["y"] + target_box["height"] / 2,
        steps=10,
    )
    page.mouse.up()


    