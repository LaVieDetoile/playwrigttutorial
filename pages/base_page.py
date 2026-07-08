from __future__ import annotations

from playwright.sync_api import Locator, Page, expect


class BasePage:
    """Base page object with shared Playwright actions."""

    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self, path: str = "/") -> None:
        self.page.goto(path, wait_until="domcontentloaded")

    def by_test_id(self, test_id: str) -> Locator:
        return self.page.get_by_test_id(test_id)

    def expect_visible(self, locator: Locator) -> None:
        expect(locator).to_be_visible()

    def fill(self, locator: Locator, value: str) -> None:
        self.expect_visible(locator)
        locator.fill(value)

    def click(self, locator: Locator) -> None:
        self.expect_visible(locator)
        locator.click()
