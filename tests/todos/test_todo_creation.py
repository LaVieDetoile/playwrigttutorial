import pytest

from pages.todo_page import TodoPage
from utils.constants import TODO_BUY_MILK, TODO_REVIEW_REPORT, TODO_WRITE_TESTS
from utils.test_data import DEFAULT_TODOS


@pytest.mark.smoke
def test_todo_app_loads(todo_page: TodoPage) -> None:
    todo_page.load()


@pytest.mark.smoke
def test_create_single_todo(todo_page: TodoPage) -> None:
    todo_page.load()
    todo_page.add_todo(TODO_BUY_MILK)

    todo_page.expect_todo_count(1)
    todo_page.expect_todo_visible(TODO_BUY_MILK)
    todo_page.expect_items_left("1 item left")


@pytest.mark.regression
def test_create_multiple_todos(todo_page: TodoPage) -> None:
    todo_page.load()
    todo_page.add_todos(DEFAULT_TODOS)

    todo_page.expect_todo_count(3)
    todo_page.expect_todo_visible(TODO_BUY_MILK)
    todo_page.expect_todo_visible(TODO_WRITE_TESTS)
    todo_page.expect_todo_visible(TODO_REVIEW_REPORT)
    todo_page.expect_items_left("3 items left")
