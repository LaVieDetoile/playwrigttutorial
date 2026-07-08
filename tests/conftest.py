from __future__ import annotations

import pytest
from playwright.sync_api import Browser, BrowserContext, Page

from pages.todo_page import TodoPage
from utils.constants import BASE_URL
from utils.test_data import DEFAULT_TODOS


@pytest.fixture()
def context(browser: Browser) -> BrowserContext:
    context = browser.new_context(base_url=BASE_URL, viewport={"width": 1440, "height": 900})
    yield context
    context.close()


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page


@pytest.fixture()
def todo_page(page: Page) -> TodoPage:
    return TodoPage(page)


@pytest.fixture()
def todo_page_with_items(todo_page: TodoPage) -> TodoPage:
    todo_page.load()
    todo_page.add_todos(DEFAULT_TODOS)
    todo_page.expect_todo_count(len(DEFAULT_TODOS))
    return todo_page
