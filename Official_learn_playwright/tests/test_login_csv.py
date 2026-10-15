import csv
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

# Get the CSV path relative to this Python file
CSV_FILE = Path(__file__).parent.parent / "test_data" / "login_data.csv"

LOGIN_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


def get_csv_data():
    """Read usernames, passwords, and expected results from CSV."""
    with CSV_FILE.open(mode="r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


@pytest.mark.parametrize("test_data", get_csv_data())
def test_login_with_csv_data(page: Page, test_data: dict) -> None:

    username = test_data["username"]
    password = test_data["password"]
    expected_result = test_data["expected_result"]

    # Open the login page
    page.goto(LOGIN_URL)

    # Enter username
    page.get_by_role("textbox", name="Username").fill(username)

    # Enter password
    page.get_by_role("textbox", name="Password").fill(password)

    # Click Login
    page.get_by_role("button", name="Login").click()

    if expected_result == "success":
        # Successful login should navigate to the dashboard
        expect(page).to_have_url(lambda url: "/dashboard" in url)

        expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()

    else:
        # Invalid or missing credentials should show an error
        expect(page.get_by_text("Invalid credentials", exact=True)).to_be_visible()
