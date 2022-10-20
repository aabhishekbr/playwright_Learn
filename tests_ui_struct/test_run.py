from playwright.sync_api import Page, expect
import pytest

@pytest.mark.xfail(reason="Code issue")
def test_example(page: Page) -> None:

    # Go to https://floward.com/
    page.goto("https://floward.com/")

    # Click img[alt="Saudi Arabia"]
    page.locator("img[alt=\"Saudi Arabia\"]").click()

    # Click img[alt="Jeddah"]
    page.locator("img[alt=\"Jeddah\"]").click()
    expect(page).to_have_url("https://floward.com/en-sa/jeddah")

    # Click [data-testid="TestId__HeaderLoginLink"]
    page.locator("[data-testid=\"TestId__HeaderLoginLink\"]").click()
    #expect(page).to_have_url("https://floward.com/en-sa/jeddah/login?url=/en-sa/jeddah")

    # Click input[name="email"]
    page.locator("input[name=\"email\"]").click()

    # Fill input[name="email"]
    page.locator("input[name=\"email\"]").fill("abhishek.roy@floward.com")

    # Press Tab
    page.locator("input[name=\"email\"]").press("Tab")

    # Fill input[name="password"]
    page.locator("input[name=\"password\"]").fill("Abhi@123")

    # Click button:has-text("Login")
    page.locator("button:has-text(\"Login\")").click()
    #expect(page).to_have_url("https://floward.com/en-sa/jeddah")

    # Go to https://floward.com/en-sa/jeddah
    page.goto("https://floward.com/en-sa/jeddah")

    # Click [data-testid="TestId__HeaderAccountButton"]
    page.locator("[data-testid=\"TestId__HeaderAccountButton\"]").click()

    # Click text=Logout
    page.locator("text=Logout").click()
    #expect(page).to_have_url("https://floward.com/en-sa/jeddah")

@pytest.mark.skip(reason="Not ready")
def test_example_skip(page: Page) -> None:

    # Go to https://floward.com/
    page.goto("https://floward.com/")

    # Click img[alt="Saudi Arabia"]
    page.locator("img[alt=\"Saudi Arabia\"]").click()

    # Click img[alt="Jeddah"]
    page.locator("img[alt=\"Jeddah\"]").click()
    expect(page).to_have_url("https://floward.com/en-sa/jeddah")

    # Click [data-testid="TestId__HeaderLoginLink"]
    page.locator("[data-testid=\"TestId__HeaderLoginLink\"]").click()
    #expect(page).to_have_url("https://floward.com/en-sa/jeddah/login?url=/en-sa/jeddah")

    # Click input[name="email"]
    page.locator("input[name=\"email\"]").click()

    # Fill input[name="email"]
    page.locator("input[name=\"email\"]").fill("abhishek.roy@floward.com")

    # Press Tab
    page.locator("input[name=\"email\"]").press("Tab")

    # Fill input[name="password"]
    page.locator("input[name=\"password\"]").fill("Abhi@123")

    # Click button:has-text("Login")
    page.locator("button:has-text(\"Login\")").click()
    #expect(page).to_have_url("https://floward.com/en-sa/jeddah")

    # Go to https://floward.com/en-sa/jeddah
    page.goto("https://floward.com/en-sa/jeddah")

    # Click [data-testid="TestId__HeaderAccountButton"]
    page.locator("[data-testid=\"TestId__HeaderAccountButton\"]").click()

    # Click text=Logout
    page.locator("text=Logout").click()
    #expect(page).to_have_url("https://floward.com/en-sa/jeddah")