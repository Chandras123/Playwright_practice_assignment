from playwright.sync_api import expect
from pages.amazon_home_page import AmazonHomePage
from pages.amazon_auth_page import AmazonAuthPage
from pages.amazon_search_results_page import AmazonSearchResultsPage
from pages.amazon_product_page import AmazonProductPage
from pages.amazon_cart_page import AmazonCartPage


# from test_data.amazon_test_data import SEARCH_PRODUCT,TARGET_PRODUCT
from test_data.amazon_test_data import SEARCH_PRODUCT, TARGET_PRODUCT

def test_amazon_product_navigation(amazon_home_page,amazon_auth_page,amazon_search_results_page,amazon_product_page,amazon_cart_page):
    # Open Amazon
    amazon_home_page.open()

    # Open authentication page
    amazon_home_page.open_auth()

    # Verify authentication page
    expect(amazon_auth_page.email_input).to_be_visible()

    # Return to Amazon home page
    amazon_auth_page.go_back()

    # Search for product
    amazon_home_page.search_product(SEARCH_PRODUCT)

    # Identify and open target product
    amazon_search_results_page.open_product(TARGET_PRODUCT)

    # Verify product detail page
    amazon_product_page.verify_product_opened()

    # Add product to cart
    amazon_product_page.add_to_cart()

    # Open cart
    amazon_home_page.open_cart()

    # Verify target product is in cart
    amazon_cart_page.verify_product_in_cart(TARGET_PRODUCT)

    # Proceed to checkout
    amazon_cart_page.proceed_to_buy()

    # Verify checkout authentication page
    expect(amazon_auth_page.email_input).to_be_visible()