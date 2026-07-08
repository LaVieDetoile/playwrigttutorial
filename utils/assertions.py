from __future__ import annotations

from pages.todo_page import TodoPage


def assert_visible_todos(todo_page: TodoPage, expected_titles: list[str]) -> None:
    for title in expected_titles:
        todo_page.expect_todo_visible(title)


def assert_hidden_todos(todo_page: TodoPage, hidden_titles: list[str]) -> None:
    for title in hidden_titles:
        todo_page.expect_todo_not_visible(title)
