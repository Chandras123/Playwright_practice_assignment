import pytest

from pages.amazon_auth_page import AmazonAuthPage
from pages.amazon_cart_page import AmazonCartPage
from pages.amazon_home_page import AmazonHomePage
from pages.amazon_product_page import AmazonProductPage
from pages.amazon_search_results_page import AmazonSearchResultsPage


@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False,
        "args": [
            "--start-maximized",
        ],
    }


@pytest.fixture
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "no_viewport": True,
    }


@pytest.fixture
def amazon_home_page(page):
    return AmazonHomePage(page)


@pytest.fixture
def amazon_auth_page(page):
    return AmazonAuthPage(page)


@pytest.fixture
def amazon_search_results_page(page):
    return AmazonSearchResultsPage(page)


@pytest.fixture
def amazon_product_page(page):
    return AmazonProductPage(page)


@pytest.fixture
def amazon_cart_page(page):
    return AmazonCartPage(page)