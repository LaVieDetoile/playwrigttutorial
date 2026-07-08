import pytest

from pages.todo_page import TodoPage
from utils.constants import TODO_BUY_MILK, TODO_REVIEW_REPORT, TODO_WRITE_TESTS
from utils.test_data import UPDATED_TODO_TITLE


@pytest.mark.e2e
@pytest.mark.regression
def test_end_to_end_todo_workflow(todo_page: TodoPage) -> None:
    todo_page.load()
    todo_page.add_todo(TODO_BUY_MILK)
    todo_page.add_todo(TODO_WRITE_TESTS)
    todo_page.add_todo(TODO_REVIEW_REPORT)
    todo_page.expect_items_left("3 items left")

    todo_page.complete_todo(TODO_BUY_MILK)
    todo_page.edit_todo(TODO_WRITE_TESTS, UPDATED_TODO_TITLE)
    todo_page.filter_active()
    todo_page.expect_todo_visible(UPDATED_TODO_TITLE)
    todo_page.expect_todo_visible(TODO_REVIEW_REPORT)
    todo_page.expect_todo_not_visible(TODO_BUY_MILK)

    todo_page.filter_completed()
    todo_page.expect_todo_visible(TODO_BUY_MILK)

    todo_page.clear_completed()
    todo_page.filter_all()
    todo_page.expect_todo_count(2)
    todo_page.expect_items_left("2 items left")
