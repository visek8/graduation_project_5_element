import allure

from page.OplataIDostavkaPage import OplataIDostavkaPage


@allure.title("check for correct answer")
def test_installation(browser_chrome, open_oplata_i_dostavka_page):
    element = OplataIDostavkaPage(browser_chrome)
    element.click_installation()
    element.text_installation()


@allure.title("check for correct answer")
def test_card(browser_chrome, open_oplata_i_dostavka_page):
    element = OplataIDostavkaPage(browser_chrome)
    element.click_card()
    element.text_card()


@allure.title("check for correct answer")
def test_kredit(browser_chrome, open_oplata_i_dostavka_page):
    element = OplataIDostavkaPage(browser_chrome)
    element.click_kredit()
    element.text_kredit()


@allure.title("check for correct answer")
def test_bank_card(browser_chrome, open_oplata_i_dostavka_page):
    element = OplataIDostavkaPage(browser_chrome)
    element.click_bank_card()
    element.text_bank_card()


@allure.title("check for correct answer")
def test_erip(browser_chrome, open_oplata_i_dostavka_page):
    element = OplataIDostavkaPage(browser_chrome)
    element.click_erip()
    element.text_erip()


@allure.title("check for correct answer")
def test_cashless(browser_chrome, open_oplata_i_dostavka_page):
    element = OplataIDostavkaPage(browser_chrome)
    element.click_cashless()
    element.text_cashless()


@allure.title("check for correct answer")
def test_app(browser_chrome, open_oplata_i_dostavka_page):
    element = OplataIDostavkaPage(browser_chrome)
    element.click_app()
    element.text_app()


@allure.title("buttons test")
def test_pickup(browser_chrome, open_oplata_i_dostavka_page):
    element = OplataIDostavkaPage(browser_chrome)
    element.pickup()
    element.city()
    element.close()
    element.mogilev()
    element.shop_mogilev()


@allure.title("Api_request_context")
def test_to_home(browser_chrome, open_oplata_i_dostavka_page):
    element = OplataIDostavkaPage(browser_chrome)
    element.pickup()
    element.to_home()
    element.delivery_terms()
    element.answer()


@allure.title("error when entering incorrect data")
def test_my_order(browser_chrome, open_oplata_i_dostavka_page):
    element = OplataIDostavkaPage(browser_chrome)
    element.my_order()
    element.phone()
    element.order_num()
    element.button_order()
    element.error()
