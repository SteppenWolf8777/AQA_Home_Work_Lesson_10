import allure
from selene import be, browser, by, have


@allure.title("Проверяем название Test Issue")
def test_github():
    browser.open("https://github.com/")
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").should(be.visible)
    browser.element("#query-builder-test").send_keys(
        "SteppenWolf8777/AQA_Home_Work_Lesson_10"
    )
    browser.element("#query-builder-test").submit()

    browser.element(by.link_text("SteppenWolf8777/AQA_Home_Work_Lesson_10")).click()

    browser.element("#issues-tab").click()