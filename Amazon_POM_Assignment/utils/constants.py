AMAZON_BASE_URL = "https://www.amazon.in/"

# Home page
AMAZON_ACCOUNT = "#nav-link-accountList"
AMAZON_SEARCH_BOX = "#twotabsearchtextbox:visible"
AMAZON_SEARCH_BUTTON = "#nav-search-bar-form #nav-search-submit-button"
AMAZON_CART = "#nav-cart"

# Authentication
AMAZON_AUTH_EMAIL = "#ap_email_login"
AMAZON_AUTH_CONTINUE = "#continue input[type='submit']"

# Search results
AMAZON_PRODUCT_RESULT = "//h2[contains(normalize-space(.), '{}')]"

# Cart
AMAZON_CART_ITEM = "li.sc-list-item"
AMAZON_PROCEED_TO_BUY = "//input[@name='proceedToRetailCheckout' and @type='submit' and @value='Proceed to checkout']"

AMAZON_ADD_TO_CART = "input#add-to-cart-button:visible"

AMAZON_CART_PRODUCT = "//li[contains(@class,'sc-item-product-title-cont')][.//span[contains(@class,'sc-grid-item-product-title') and contains(normalize-space(.), '{}')]]"
