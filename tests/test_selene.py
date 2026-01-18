import allure
from selene import be, browser, by, have
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--user-data-dir=/tmp/chrome-profile")  # если нужно
browser.config.driver = webdriver.Chrome(options=options)


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