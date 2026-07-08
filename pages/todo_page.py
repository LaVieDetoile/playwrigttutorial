from __future__ import annotations

from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage


class TodoPage(BasePage):
    """Page object for the public Playwright TodoMVC demo app."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.new_todo_input: Locator = page.get_by_placeholder("What needs to be done?")
        self.todo_items: Locator = page.locator(".todo-list li")
        self.todo_count: Locator = page.locator(".todo-count")
        self.clear_completed_button: Locator = page.get_by_role("button", name="Clear completed")

    def load(self) -> None:
        self.open("")
        expect(self.new_todo_input).to_be_visible()

    def add_todo(self, title: str) -> None:
        self.new_todo_input.fill(title)
        self.new_todo_input.press("Enter")

    def add_todos(self, titles: list[str]) -> None:
        for title in titles:
            self.add_todo(title)

    def todo_by_title(self, title: str) -> Locator:
        return self.todo_items.filter(has_text=title)

    def expect_todo_visible(self, title: str) -> None:
        expect(self.todo_by_title(title)).to_be_visible()

    def expect_todo_not_visible(self, title: str) -> None:
        expect(self.todo_by_title(title)).to_have_count(0)

    def expect_todo_count(self, expected_count: int) -> None:
        expect(self.todo_items).to_have_count(expected_count)

    def expect_items_left(self, expected_text: str) -> None:
        expect(self.todo_count).to_have_text(expected_text)

    def complete_todo(self, title: str) -> None:
        self.todo_by_title(title).locator(".toggle").check()

    def expect_todo_completed(self, title: str) -> None:
        expect(self.todo_by_title(title)).to_have_class("completed")

    def delete_todo(self, title: str) -> None:
        todo = self.todo_by_title(title)
        todo.hover()
        todo.locator(".destroy").click()

    def edit_todo(self, current_title: str, new_title: str) -> None:
        todo = self.todo_by_title(current_title)
        todo.dblclick()
        edit_input = todo.locator(".edit")
        edit_input.fill(new_title)
        edit_input.press("Enter")

    def filter_active(self) -> None:
        self.page.get_by_role("link", name="Active").click()

    def filter_completed(self) -> None:
        self.page.get_by_role("link", name="Completed").click()

    def filter_all(self) -> None:
        self.page.get_by_role("link", name="All").click()

    def clear_completed(self) -> None:
        self.clear_completed_button.click()
