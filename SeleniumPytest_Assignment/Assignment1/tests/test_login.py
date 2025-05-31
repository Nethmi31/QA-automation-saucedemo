import pytest
from pages.login_page import LoginPage

@pytest.mark.login
def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.load("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in browser.current_url