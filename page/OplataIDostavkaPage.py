import allure

from page.BasePage import BasePage


class OplataIDostavkaPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.INSTALLATION = '//*[@id="thumb-payment-payment_475d6bca-9c2d-11e6-80df-005056842056"]'
        self.TEXT_INSTALLATION = 'Рассрочка в розничном магазине'

        self.CARD = '//*[@id="thumb-payment-payment_b36df7e5-9c2c-11e6-80df-005056842056"]'
        self.TEXT_CARD = 'Оплата картой рассрочки в розничном магазине'

        self.KREDIT = '//*[@id="thumb-payment-payment_1caddf28-abf0-11e6-80df-005056842056"]'
        self.TEXT_KREDIT = 'Кредит в розничном магазине'

        self.BANK_CARD = '//*[@id="thumb-payment-payment_5619be54-f054-11e7-80c4-005056840c70"]'
        self.TEXT_BANK_CARD = 'Оплата банковской картой онлайн'

        self.ERIP = '//*[@id="thumb-payment-payment_a14bc0b7-9c2d-11e6-80df-005056842056"]'
        self.TEXT_ERIP = 'Система «Расчет» (ЕРИП)'

        self.CASHLESS = '//*[@id="thumb-payment-payment_d89bfa60-9c2b-11e6-80df-005056842056"]'
        self.TEXT_CASHLESS = 'Безналичный расчет'

        self.APP = '//*[@id="thumb-payment-payment_25959279-7dab-11ec-bb92-005056012463"]'
        self.TEXT_APP = 'Оплата через приложение Оплати'

        self.PICKUP = '//*[@class="nav-link"]'
        self.CITY = '//*[@class="inp-ic-autocomplite inp-ic-toggle delivery-autocomplete"]'
        self.CLOSE = '//*[@class="inp-ic-close__icon"]'
        self.MOGILEV = 'Могилев'
        self.SHOP_MOGILEV = 'ул. Лазаренко, 73Б (ТЦ «Армада»)'

        self.TO_HOME = '//*[@id="thumb-payment-2739"]'
        self.DELIVERY_TERMS = '//*[@id="thumb-delivery-2"]'
        self.ANSWER = '//*[@id="tab-delivery-2"]'

        self.MY_ORDER = '//*/div[1]/div/div/div[3]/ul/li[5]'
        self.PHONE_NUM = '//*/div[6]/div/div[2]/form/div[1]/input'
        self.ORDER_NUM = '//*[@type="number"]'
        self.BUTTON_ORDER = '//*/form/div[3]/button'
        self.ERROR = 'Ошибка'

    @allure.step("Click to my order")
    def my_order(self):
        self.click(self.MY_ORDER)

    @allure.step("entering a phone number")
    def phone(self):
        self.fill_field(self.PHONE_NUM, '333333333')

    @allure.step("order number entry")
    def order_num(self):
        self.fill_field(self.ORDER_NUM, '88')

    @allure.step("button click")
    def button_order(self):
        self.click(self.BUTTON_ORDER)

    @allure.step("error message")
    def error(self):
        self.assert_that_text_is_displayed(self.ERROR)

    @allure.step("click to home")
    def to_home(self):
        self.click(self.TO_HOME)

    @allure.step("click to delivery terms")
    def delivery_terms(self):
        self.click(self.DELIVERY_TERMS)

    @allure.step("check answer")
    def answer(self):
        self.assert_that_element_is_displayed(self.ANSWER)

    @allure.step("click to pickup")
    def pickup(self):
        self.click(self.PICKUP)

    @allure.step("click to city")
    def city(self):
        self.click(self.CITY)

    @allure.step("delete selected city")
    def close(self):
        self.click(self.CLOSE)

    @allure.step("select Mogilev")
    def mogilev(self):
        self.click_text(self.MOGILEV)

    @allure.step("check shop in Mogilev")
    def shop_mogilev(self):
        self.assert_that_text_is_displayed(self.SHOP_MOGILEV)

    @allure.step("click to app")
    def click_app(self):
        self.click(self.APP)

    @allure.step("check answer")
    def text_app(self):
        self.assert_that_text_is_displayed(self.TEXT_APP)

    @allure.step("click to cashless")
    def click_cashless(self):
        self.click(self.CASHLESS)

    @allure.step("check answer")
    def text_cashless(self):
        self.assert_that_text_is_displayed(self.TEXT_CASHLESS)

    @allure.step("click to ERIP")
    def click_erip(self):
        self.click(self.ERIP)

    @allure.step("check answer")
    def text_erip(self):
        self.assert_that_text_is_displayed(self.TEXT_ERIP)

    @allure.step("click to bank card")
    def click_bank_card(self):
        self.click(self.BANK_CARD)

    @allure.step("check answer")
    def text_bank_card(self):
        self.assert_that_text_is_displayed(self.TEXT_BANK_CARD)

    @allure.step("click to kredit")
    def click_kredit(self):
        self.click(self.KREDIT)

    @allure.step("check answer")
    def text_kredit(self):
        self.assert_that_text_is_displayed(self.TEXT_KREDIT)

    @allure.step("click to card")
    def click_card(self):
        self.click(self.CARD)

    @allure.step("check answer")
    def text_card(self):
        self.assert_that_text_is_displayed(self.TEXT_CARD)

    @allure.step("click to installation")
    def click_installation(self):
        self.click(self.INSTALLATION)

    @allure.step("check answer")
    def text_installation(self):
        self.assert_that_text_is_displayed(self.TEXT_INSTALLATION)
