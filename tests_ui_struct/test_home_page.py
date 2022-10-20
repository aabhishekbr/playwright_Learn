from playwright.sync_api import expect
import pytest
from pom.login_page_elements import LoginPage
@pytest.mark.regression
def test_run_with_fix(navigate_to_login_setup)->None:
    page=navigate_to_login_setup
    # Click text=Logout
    page.locator("text=Logout").click()




