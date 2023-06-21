from pathlib import Path
import allure
from allure import attachment_type
from slugify import slugify
import pytest
from selenium import webdriver


@pytest.fixture
def browser_chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    yield driver

    driver.close()
    driver.quit()


@pytest.fixture
def open_page(browser_chrome):
    browser_chrome.get("https://5element.by/")
    browser_chrome.maximize_window()


@pytest.fixture
def open_shops_page(browser_chrome):
    browser_chrome.get("https://5element.by/shops")
    browser_chrome.maximize_window()


@pytest.fixture
def open_help_page(browser_chrome):
    browser_chrome.get("https://5element.by/help")
    browser_chrome.maximize_window()


@pytest.fixture
def open_oplata_i_dostavka_page(browser_chrome):
    browser_chrome.get("https://5element.by/services/1003-oplata-i-dostavka")
    browser_chrome.maximize_window()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    screen_file = ''
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        if report.failed and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
            page.screenshot(path=screen_file)
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            allure.attach.file(screen_file, name="screenshot",
                               attachment_type=attachment_type.PNG)
        report.extra = extra
