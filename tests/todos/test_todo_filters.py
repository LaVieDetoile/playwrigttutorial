import pytest

from pages.todo_page import TodoPage
from utils.assertions import assert_hidden_todos, assert_visible_todos
from utils.constants import TODO_BUY_MILK, TODO_REVIEW_REPORT, TODO_WRITE_TESTS


@pytest.mark.regression
def test_active_filter_shows_only_incomplete_todos(todo_page_with_items: TodoPage) -> None:
    todo_page_with_items.complete_todo(TODO_BUY_MILK)
    todo_page_with_items.filter_active()

    assert_visible_todos(todo_page_with_items, [TODO_WRITE_TESTS, TODO_REVIEW_REPORT])
    assert_hidden_todos(todo_page_with_items, [TODO_BUY_MILK])


@pytest.mark.regression
def test_completed_filter_shows_only_completed_todos(todo_page_with_items: TodoPage) -> None:
    todo_page_with_items.complete_todo(TODO_BUY_MILK)
    todo_page_with_items.filter_completed()

    assert_visible_todos(todo_page_with_items, [TODO_BUY_MILK])
    assert_hidden_todos(todo_page_with_items, [TODO_WRITE_TESTS, TODO_REVIEW_REPORT])


@pytest.mark.regression
def test_all_filter_shows_all_todos(todo_page_with_items: TodoPage) -> None:
    todo_page_with_items.complete_todo(TODO_BUY_MILK)
    todo_page_with_items.filter_completed()
    todo_page_with_items.filter_all()

    assert_visible_todos(todo_page_with_items, [TODO_BUY_MILK, TODO_WRITE_TESTS, TODO_REVIEW_REPORT])
