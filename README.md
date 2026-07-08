# Playwright Tutorial Portfolio

A public Playwright Python automation project that demonstrates professional end-to-end UI testing practices against the Playwright TodoMVC demo app.

## Project Purpose

This repository is designed as an interview-ready portfolio project. It shows how to organize Playwright tests with Pytest, Page Object Model, reusable fixtures, feature-based test folders, stable selectors, meaningful assertions, linting, reporting, and CI.

## Website Under Test

[Playwright TodoMVC Demo](https://demo.playwright.dev/todomvc) is a public demo application used by the Playwright project. It supports adding, editing, completing, filtering, clearing, and deleting todo items, which makes it useful for focused UI automation practice.

## Public Portfolio Disclaimer

This project uses only public demo applications and does not contain company code, credentials, internal URLs, or proprietary logic.

## Tech Stack

- Python
- Playwright for Python
- Pytest
- pytest-playwright
- pytest-html
- Poetry
- Ruff
- GitHub Actions

## Folder Structure

```text
playwrigttutorial/
  pages/
    base_page.py
    todo_page.py
  tests/
    conftest.py
    todos/
      test_todo_creation.py
      test_todo_completion.py
      test_todo_editing.py
      test_todo_filters.py
    e2e/
      test_todo_workflow.py
  utils/
    constants.py
    test_data.py
    assertions.py
  .github/workflows/playwright-tests.yml
  .env.sample
  .gitignore
  pyproject.toml
  pytest.ini
```

## Test Coverage

### Todo Creation

- App loads successfully
- Create a single todo
- Create multiple todos
- Validate visible todo titles and item counters

### Todo Completion

- Complete a todo and verify completed state
- Verify remaining item counter updates
- Clear completed todos

### Todo Editing and Deletion

- Edit an existing todo title
- Delete an existing todo
- Verify deleted todos are removed from the list

### Todo Filters

- Active filter shows only incomplete todos
- Completed filter shows only completed todos
- All filter shows all todos

### E2E Workflow

- Load app
- Add multiple todos
- Complete a todo
- Edit a todo
- Filter active/completed/all
- Clear completed
- Verify final list and counter

## Install

```bash
poetry install
poetry run playwright install chromium
```

Optional local environment file:

```bash
cp .env.sample .env
```

Do not commit `.env`.

## Run Tests

```bash
poetry run pytest
poetry run pytest -m smoke
poetry run pytest -m regression
poetry run pytest -m e2e
```

## Headed and Debug Mode

```bash
poetry run pytest --headed
poetry run pytest --headed --slowmo 300
PWDEBUG=1 poetry run pytest tests/e2e/test_todo_workflow.py
```

## Lint and Format

```bash
poetry run ruff check .
poetry run ruff format .
```

## Reports and Artifacts

The project uses Playwright/Pytest artifact settings:

- Screenshots only on failure
- Videos retained on failure
- Traces retained on failure
- HTML report generated at `reports/playwright-report.html`

Generated reports and test artifacts are ignored by git.

## CI

GitHub Actions runs on `push` and `pull_request`. The workflow:

1. Checks out the repository.
2. Installs Python.
3. Installs Poetry dependencies.
4. Installs Playwright Chromium.
5. Runs Ruff lint checks.
6. Runs the Playwright test suite.
7. Uploads the HTML report and failure artifacts when appropriate.

## What Interviewers Should Notice

- Clean Page Object Model design
- Feature-based test organization
- Shared fixture setup for independent tests
- Stable accessible selectors and CSS selectors scoped inside page objects
- No arbitrary sleeps
- Clear assertions and readable test names
- CI-ready configuration
- Public-safe test data and documentation
