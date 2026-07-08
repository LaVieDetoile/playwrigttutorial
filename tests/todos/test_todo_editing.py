import pytest

from pages.todo_page import TodoPage
from utils.constants import TODO_WRITE_TESTS
from utils.test_data import UPDATED_TODO_TITLE


@pytest.mark.regression
def test_edit_existing_todo(todo_page_with_items: TodoPage) -> None:
    todo_page_with_items.edit_todo(TODO_WRITE_TESTS, UPDATED_TODO_TITLE)

    todo_page_with_items.expect_todo_not_visible(TODO_WRITE_TESTS)
    todo_page_with_items.expect_todo_visible(UPDATED_TODO_TITLE)


@pytest.mark.regression
def test_delete_existing_todo(todo_page_with_items: TodoPage) -> None:
    todo_page_with_items.delete_todo(TODO_WRITE_TESTS)

    todo_page_with_items.expect_todo_not_visible(TODO_WRITE_TESTS)
    todo_page_with_items.expect_todo_count(2)
    todo_page_with_items.expect_items_left("2 items left")
