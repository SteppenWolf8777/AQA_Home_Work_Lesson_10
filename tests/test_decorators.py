import allure
import pytest
from selene import browser, have


@allure.step("Открыть страницу Issues репозитория: {repo}")
def open_issues_page(repo):
    browser.open(f"https://github.com/{repo}/issues")


@allure.step("Открыть Issue по заголовку: {title}")
def open_issue_by_title(title):
    browser.all('[data-testid="issue-pr-title-link"]').element_by(
        have.exact_text(title)
    ).click()


@allure.step("Проверить заголовок Issue равный: {expected_title}")
def should_have_issue_title(expected_title):
    browser.element('[data-testid="issue-title"]').should(
        have.exact_text(expected_title)
    )


def test_issue_title_is_visible():
    repo = "SteppenWolf8777/AQA_Home_Work_Lesson_9"
    expected_title = "AQA_Home_Work_Lesson_9"

    open_issues_page(repo)
    open_issue_by_title(expected_title)
    should_have_issue_title(expected_title)