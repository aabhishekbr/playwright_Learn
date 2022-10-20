from playwright.sync_api import Page, expect, Playwright
class LoginPage:
    def __init__(self, page):
        self.page=page
        self.Email = page.locator("input[name=\"email\"]")
        self.Password = page.locator("input[name=\"password\"]")
