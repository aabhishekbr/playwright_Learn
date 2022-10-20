import pytest
from playwright.sync_api import Page, expect, Playwright
import pytest
useremail="aabhishekbr@gmail.com"
password="Abhi@123"
from pom.login_page_elements import LoginPage

@pytest.mark.parametrize("useremail,password",[("aaa,123"),("aabhishekbr@gmail.com,Abhi@123")])
@pytest.fixture(scope="session")
def set_up(browser) -> None:
    context=browser.new_context()
    page=context.new_page()
    # Go to https://beta.floward.com/
    page.goto("https://beta.floward.com/")
    page.wait_for_load_state()
    page.set_default_timeout(4000)
    yield page
    page.close()

@pytest.fixture(scope="session")
def navigate_to_login_setup(set_up):
    page = set_up
    Login_Page = LoginPage(page)

    # Click img[alt="Kuwait"]
    page.locator("img[alt=\"Kuwait\"]").click()
    page.wait_for_url("https://beta.floward.com/en-kw")

    # Click text=Login
    page.locator("text=Login").click()
    page.wait_for_url("https://beta.floward.com/en-kw/login?url=%2Fen-kw")

    # Click input[name="email"]
    Login_Page.Email.click()

    # Fill input[name="email"]
    Login_Page.Email.fill(useremail)
    # Press Tab
    Login_Page.Email.press("Tab")
    # Fill input[name="password"]
    Login_Page.Password.fill(password)

    # Click button:has-text("Login")
    page.locator("button:has-text(\"Login\")").click()
    page.wait_for_url("https://beta.floward.com/en-kw")

    # Click text=Login Succes
    page.locator("text=Login Succes").click()

    # Click text=Welcome, Abhishek
    expect(page.locator(f"text=Welcome, Abhishek")).to_be_visible()
    page.locator(f"text=Welcome, Abhishek").click()
    yield page

