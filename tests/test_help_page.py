import allure

from page.HelpPage import HelpPage


@allure.title("answer protect check")
def test_protect(browser_chrome, open_help_page):
    element = HelpPage(browser_chrome)
    element.click_protect()
    element.pic_protect()


@allure.title("answer product check")
def test_product(browser_chrome, open_help_page):
    element = HelpPage(browser_chrome)
    element.click_product()
    element.pic_product()


@allure.title("answer bonus check")
def test_liquidation(browser_chrome, open_help_page):
    element = HelpPage(browser_chrome)
    element.click_liquidation()
    element.text_bonus()


@allure.title("answer kredit check")
def test_kredit(browser_chrome, open_help_page):
    element = HelpPage(browser_chrome)
    element.click_kredit()
    element.text_kredit()


@allure.title("answer deliver check")
def test_deliver(browser_chrome, open_help_page):
    element = HelpPage(browser_chrome)
    element.click_deliver()
    element.text_deliver()


@allure.title("answer order check")
def test_order(browser_chrome, open_help_page):
    element = HelpPage(browser_chrome)
    element.click_order()
    element.pic_order()


@allure.title("answer add_comment check")
def test_comment(browser_chrome, open_help_page):
    element = HelpPage(browser_chrome)
    element.click_comment()
    element.pic_comment()


@allure.title("answer py cashless check")
def test_cashless(browser_chrome, open_help_page):
    element = HelpPage(browser_chrome)
    element.click_cashless()
    element.text_cashless()
