from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://finfolks.com/login")
    page.get_by_label("E-Mail Address").click()
    page.get_by_label("E-Mail Address").fill("admin@finfolks.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("ccmd5#238")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Profile image").click()
 
    page.get_by_role("link", name=" Logout").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
