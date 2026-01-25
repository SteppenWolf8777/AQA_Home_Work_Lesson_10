import allure
from selene import be, browser, by, have


@allure.title("Проверяем название Test Issue")
@allure.epic("GitHub")
@allure.feature("Репозиторий")
@allure.story("Поиск issues")
@allure.tag("issue")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "SteppenWolf8777")
@allure.description("Проверка наличия issue с нужным именем")
@allure.link(
    "SteppenWolf8777/AQA_Home_Work_Lesson_10",
    name="Issue Link",
)
def test_github():
    open_github()
    search_repository()
    open_repository()
    open_issues()
    find_name_issue()


@allure.step("Открыть Github")
def open_github():
    browser.open("https://github.com/")


@allure.step("Найти репозиторий с дз 10")
def search_repository():
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").should(be.visible)
    browser.element("#query-builder-test").send_keys(
        "SteppenWolf8777/AQA_Home_Work_Lesson_10"
    )
    browser.element("#query-builder-test").submit()


@allure.step("Открыть репозиторий с дз 10")
def open_repository():
    browser.element(by.link_text("SteppenWolf8777/AQA_Home_Work_Lesson_10")).click()


@allure.step("Открыть вкладку Issues")
def open_issues():
    browser.element("#issues-tab").click()


@allure.step('Найти issue с заголовком "test issues"')
def find_name_issue():
    browser.element("[data-testid='issue-pr-title-link']").should(
        have.text("test issues")
    )