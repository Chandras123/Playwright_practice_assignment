from playwright.sync_api import Page, expect


def test_mocking_api(page: Page):
    page.route("**/api/v1/fruits", lambda route: route.fulfill(json=[{"name": "Strawberry", "id": 21}]))
    page.goto("https://demo.playwright.dev/api-mocking")
    expect(page.get_by_text("Strawberry")).to_be_visible()


def test_intercepting_request_and_modifying_it(page: Page):
    def handle_route(route):
        response = route.fetch()
        json_payload = response.json()
        json_payload.append({"name": "Playwright", "id": 100})
        route.fulfill(response=response, json=json_payload)

    page.route("**/api/v1/fruits", handle_route)
    page.goto("https://demo.playwright.dev/api-mocking")
    expect(page.get_by_text("Playwright", exact=True)).to_be_visible()


def test_mocking_with_har_files(page: Page):
    page.route_from_har("./hars/fruits.har", url="**/api/v1/fruits", update=True)
    page.goto("https://demo.playwright.dev/api-mocking")
    expect(page.get_by_text("Strawberry")).to_be_visible()


def test_mocking_with_har_files_replay(page: Page):
    page.route_from_har("./hars/fruits.har", url="**/api/v1/fruits", update=False)
    page.goto("https://demo.playwright.dev/api-mocking")
    expect(page.get_by_text("Strawberry")).to_be_visible()





def test_products_are_displayed(page: Page):
    # Intercept the application's products API
    def mock_products(route):
        route.fulfill(
            status=200,
            json=[
                {
                    "id": 1,
                    "name": "Headphones",
                    "price": 1999
                }
            ],
        )

    # Register the mock before opening the page
    page.route("**/api/products", mock_products)

    page.goto("*/demo.application/products")

    # Verify the frontend renders the mocked data
    expect(
        page.get_by_text("Headphones", exact=True)
    ).to_be_visible()

    expect(
        page.get_by_text("1999", exact=True)
    ).to_be_visible()





def test_products_network_response(page: Page):
    page.goto("*/demo.application/products")

    # Start waiting before performing the action
    with page.expect_response(                                              #except_response method is used to wait for a network response that matches a specific condition. It allows you to perform an action (like clicking a button) and then wait for the corresponding network response to be received.
        lambda response:
            "/api/products" in response.url
            and response.request.method == "GET"
    ) as response_info:

        page.get_by_role(
            "button",
            name="Refresh Products"
        ).click()

    response = response_info.value

    # Validate the network response
    assert response.status == 200

    # Validate the response data
    products = response.json()
    assert isinstance(products, list)

    # Validate the user-visible result
    expect(
        page.get_by_text("Headphones", exact=True)
    ).to_be_visible()