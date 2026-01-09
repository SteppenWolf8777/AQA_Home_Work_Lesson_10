import allure
from selene import be, browser, by, have


@allure.title("Проверяем название Test Issue")
def test_github():
    browser.open("https://github.com/")
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").should(be.visible)
    browser.element("#query-builder-test").send_keys(
        "PanovaAlyona/qa_guru_homework_10"
    )
    browser.element("#query-builder-test").submit()

    browser.element(by.link_text("PanovaAlyona/qa_guru_homework_10")).click()

    browser.element("#issues-tab").click()
    browser.element("[data-testid='issue-pr-title-link']").should(
        have.text("Test Issue")
    )