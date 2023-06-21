import allure

from page.BasePage import BasePage


class HelpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.PROTECT = '//*[@id="question-help-3763"]'
        self.PIC_PROTECT = '//*[@src="/images/2021/promo2/ris7.jpg"]'

        self.PRODUCT = '//*[@id="question-help-3561"]'
        self.PIC_PRODUCT = '//*[@src="/upload/medialibrary/9ec/9ece90f9bdf658458d2805be43af2e79.png"]'

        self.LIQUIDATION = '//*[@id="question-help-3871"]'
        self.TEXT_LIQUIDATION = '//*[@id="help-collapse-3871"]'

        self.BONUS = '//*[@id="question-help-167"]'
        self.TEXT_BONUS = '//*[@id="help-collapse-167"]'

        self.KREDIT = '//*[@id="question-help-39"]'
        self.TEXT_KREDIT = '//*[@id="help-collapse-39"]'

        self.DELIVER = '//*[@id="question-help-727"]'
        self.TEXT_DELIVER = '//*[@id="help-collapse-727"]'

        self.ORDER = '//*[@id="question-help-2559"]'
        self.PIC_ORDER = '//*[@src="/upload/medialibrary/94a/94a1000c122ee436282c59085bb9cfab.jpeg"]'

        self.COMMENT = '//*[@id="question-help-2753"]'
        self.PIC_COMMENT = '//*[@src="/upload/medialibrary/190/19056b2a58877f2b7cac4cbfc8d6c020.jpeg"]'

        self.CASHLESS = '//*[@id="question-help-1543"]'
        self.TEXT_CASHLESS = '//*[@id="help-collapse-1543"]'

    @allure.step("cashless click")
    def click_cashless(self):
        self.click(self.CASHLESS)

    @allure.step("cashless answer check")
    def text_cashless(self):
        self.assert_that_element_is_displayed(self.TEXT_CASHLESS)

    @allure.step("comment click")
    def click_comment(self):
        self.click(self.COMMENT)

    @allure.step("comment answer check")
    def pic_comment(self):
        self.assert_that_element_is_displayed(self.PIC_COMMENT)

    @allure.step("order click")
    def click_order(self):
        self.click(self.ORDER)

    @allure.step("order answer check")
    def pic_order(self):
        self.assert_that_element_is_displayed(self.PIC_ORDER)

    @allure.step("deliver click")
    def click_deliver(self):
        self.click(self.DELIVER)

    @allure.step("deliver answer check")
    def text_deliver(self):
        self.assert_that_element_is_displayed(self.TEXT_DELIVER)

    @allure.step("kredit click")
    def click_kredit(self):
        self.click(self.KREDIT)

    @allure.step("kredit answer check")
    def text_kredit(self):
        self.assert_that_element_is_displayed(self.TEXT_KREDIT)

    @allure.step("bonus click")
    def click_bonus(self):
        self.click(self.BONUS)

    @allure.step("bonus answer check")
    def text_bonus(self):
        self.assert_that_element_is_displayed(self.TEXT_BONUS)

    @allure.step("liquidation click")
    def click_liquidation(self):
        self.click(self.LIQUIDATION)

    @allure.step("liquidation answer check")
    def text_liquidation(self):
        self.assert_that_element_is_displayed(self.TEXT_LIQUIDATION)

    @allure.step("product click")
    def click_product(self):
        self.click(self.PRODUCT)

    @allure.step("product answer check")
    def pic_product(self):
        self.assert_that_element_is_displayed(self.PIC_PRODUCT)

    @allure.step("protect click")
    def click_protect(self):
        self.click(self.PROTECT)

    @allure.step("protect answer check")
    def pic_protect(self):
        self.assert_that_element_is_displayed(self.PIC_PROTECT)
