import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_label("Search", exact=True).click()
    page.get_by_label("Search", exact=True).fill("the tallest building in the world")
    page.goto("https://www.skyscrapercenter.com/buildings?gad_source=1&gclid=EAIaIQobChMIjcXLiNGMiQMVfynUAR2NiAUuEAAYASAAEgKnfPD_BwE")
    page.get_by_role("link", name="Burj Khalifa").click()
    page.locator(".rank").first.click()
    expect(page.get_by_label("Search", exact=True)).to_be_hidden()
    print("Yay!")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
