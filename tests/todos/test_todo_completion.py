import pytest

from pages.todo_page import TodoPage
from utils.constants import TODO_BUY_MILK, TODO_WRITE_TESTS


@pytest.mark.regression
def test_complete_todo_updates_state_and_counter(todo_page_with_items: TodoPage) -> None:
    todo_page_with_items.complete_todo(TODO_BUY_MILK)

    todo_page_with_items.expect_todo_completed(TODO_BUY_MILK)
    todo_page_with_items.expect_items_left("2 items left")


@pytest.mark.regression
def test_clear_completed_removes_completed_todos(todo_page_with_items: TodoPage) -> None:
    todo_page_with_items.complete_todo(TODO_BUY_MILK)
    todo_page_with_items.clear_completed()

    todo_page_with_items.expect_todo_not_visible(TODO_BUY_MILK)
    todo_page_with_items.expect_todo_visible(TODO_WRITE_TESTS)
    todo_page_with_items.expect_todo_count(2)
