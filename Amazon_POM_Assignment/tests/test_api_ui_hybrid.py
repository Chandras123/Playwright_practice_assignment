
from urllib.parse import parse_qs, urlparse

from playwright.sync_api import Page, expect


def test_api_product_data_then_amazon_search(page: Page):
    
    response = page.request.get(
        "https://dummyjson.com/products/1"
    )

  
    assert response.status == 200

    product = response.json()
    product_title = product["title"]

    assert product_title, "Product title should not be empty"


    page.goto("https://www.amazon.in/")

    search_box = page.locator("#twotabsearchtextbox")
    expect(search_box).to_be_visible()

    search_box.fill(product_title)
    search_box.press("Enter")

   
    expect(page).to_have_url(lambda url: "/s?" in url)


    query_params = parse_qs(urlparse(page.url).query)
    actual_query = query_params.get("k", [""])[0]

    assert actual_query == product_title, (
        f"Expected search query {product_title!r}, "
        f"but received {actual_query!r}"
    )

    
