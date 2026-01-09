import pytest
from selene import browser


@pytest.fixture(autouse=True)
def setup_browser():
    browser.config.window_width = 1200
    browser.config.window_height = 900
    yield
    browser.quit()