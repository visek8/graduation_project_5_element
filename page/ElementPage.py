import allure

from page.BasePage import BasePage


class ElementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.KATALOG = '//*[@class="js-mm-opener btn"]'
        self.GEO = '//*[@class="h-drop__head"]'
        self.NEW = '//*/div[3]/div/div[1]/div[1]/div[1]'
        self.KITCHEN = '//*[@aria-label="5 / 13"]'
        self.SEARCH = '//form[2]/input[2]'
        self.KITCHEN_URL = 'https://5element.by/catalog/21-tehnika-dlya-kuhni'
        self.TEXT_FOR_SEARCH = "Маркус Зусак\n"
        self.IMAGE_NOT_FOUND = '//*[@class = "section-error section-error__404"]'

        self.VENT_BANNER = '//*[@class="hero-aside-banner__decor ec-banner"]'
        self.VENT = '//*[1]/div/div[3]/div[4]/button'
        self.GO_TO_BUSKET = '//*[@id="app"]/div[9]/div/div[3]/div[2]/a[2]'
        self.VENT_COUNT = '//*[@class="input-counter-field"]'
        self.PRICE = '//*[@class="c-price"]'

        self.INSTAGRAM = '//*[@class="ic-soc-inst"]'

        self.ACTION = '//*[@class="swiper-slide swiper-slide-visible swiper-slide-active"]'
        self.CHEKBOX = '//*[@id="filter-category"]/div/div[4]/div/label/div[1]'

        self.INSTALLMENT = '//*[@href="/action/9-rassrochka/13648-rassrochka-na-18-mesyacev-s-pervym-vznosom-ot-0"]'
        self.POSTER = '//*[@class="section-stock__poster"]'

        self.LIKE = '//*[@class="n-item__icon ic-favorite"]'
        self.DROP_CONTENT = '//*[3]/div[2]/div[2]/div'

        self.COMPARE = '//*[@class="n-item__icon ic-compare"]'
        self.DROP_COMPARE = '//*[3]/div[1]/div[2]/div'

        self.ENTRY = '//*[@class="h-drop h-user"]'
        self.BUTTON_ENTRY = '//*[1]/form/div[4]/button'
        self.LOGIN = '//*[@name="login"]'
        self.PASSWORD = '//*[@type="password"]'
        self.USER_NOT_FOUND = '//*/form/div[1]/span'

        self.VIBER_ENTRY = '//*/form/div[5]/a'
        self.MOBILE_NUM = '//*[@placeholder="Номер телефона"]'
        self.SMS = '//*/form/div[2]/button'
        self.CODE = '//*[@placeholder="Код подтверждения"]'
        self.BUTTON_ENTRY_CODE = '//*/form[2]/div[2]/button'
        self.INVALID_CODE = '//*/form[2]/div[1]/span'

        self.USER_VK = '//*[@class="ic-soc-vk"]'
        self.USER_GOOGLE = '//*[@class="ic-soc-google"]'
        self.USER_YANDEX = '//*[@class="ic-soc-yandex"]'
        self.USER_FACEBOOK = '//*[@class="ic-soc-fb"]'

    @allure.step("is icon vk displayed")
    def user_vk(self):
        self.assert_that_element_is_displayed(self.USER_VK)

    @allure.step("is icon google displayed")
    def user_google(self):
        self.assert_that_element_is_displayed(self.USER_GOOGLE)

    @allure.step("is icon yandex displayed")
    def user_yandex(self):
        self.assert_that_element_is_displayed(self.USER_YANDEX)

    @allure.step("is icon facebook displayed")
    def user_facebook(self):
        self.click(self.USER_FACEBOOK)

    @allure.step("vk icon click")
    def user_vk_click(self):
        self.click(self.USER_VK)

    @allure.step("google icon click")
    def user_google_click(self):
        self.click(self.USER_GOOGLE)

    @allure.step("yandex icon click")
    def user_yandex_click(self):
        self.click(self.USER_YANDEX)

    @allure.step("facebook icon click")
    def user_facebook_click(self):
        self.click(self.USER_FACEBOOK)

    @allure.step("login with viber click")
    def viber_entry(self):
        self.click(self.VIBER_ENTRY)

    @allure.step("entering a phone number")
    def mobile_num(self):
        self.fill_field(self.MOBILE_NUM, '333333333')

    @allure.step("send sms click")
    def sms_button(self):
        self.click(self.SMS)

    @allure.step("message about invalid code is visible")
    def code(self):
        self.assert_that_element_is_displayed(self.CODE)

    @allure.step("entering a code")
    def inter_code(self):
        self.fill_field(self.CODE, "4356")

    @allure.step("click button send code")
    def entry_code(self):
        self.click(self.BUTTON_ENTRY_CODE)

    @allure.step("message about invalid code is visible")
    def invalid_code(self):
        self.assert_that_element_is_displayed(self.INVALID_CODE)

    @allure.step("click user")
    def click_user(self):
        self.click(self.ENTRY)

    @allure.step("enter email")
    def login(self):
        self.fill_field(self.LOGIN, "ivanov_ivan@rambler.ru")

    @allure.step("enter password")
    def password(self):
        self.fill_field(self.PASSWORD, "ivanov_ivan")

    @allure.step("message user not found visible")
    def user_not_found(self):
        self.assert_that_element_is_displayed(self.USER_NOT_FOUND)

    @allure.step("click button entry")
    def click_entry(self):
        self.click(self.BUTTON_ENTRY)

    @allure.step("compare click")
    def click_compare(self):
        self.click(self.COMPARE)

    @allure.step("compare message visible")
    def drop_compare(self):
        self.assert_that_element_is_displayed(self.DROP_COMPARE)

    @allure.step("like click")
    def click_like(self):
        self.click(self.LIKE)

    @allure.step("like message visible")
    def drop_like(self):
        self.assert_that_element_is_displayed(self.DROP_CONTENT)

    @allure.step("katalog click")
    def click_katalog(self):
        self.click(self.KATALOG)

    @allure.step("installment click")
    def installment(self):
        self.click(self.INSTALLMENT)

    @allure.step("poster is visible check")
    def poster(self):
        self.assert_that_element_is_displayed(self.POSTER)

    @allure.step("action click")
    def click_action(self):
        self.click(self.ACTION)

    @allure.step("checkbox click")
    def click_chekbox(self):
        self.click(self.CHEKBOX)

    @allure.step("check is checkbox selected")
    def select_checkbox(self):
        self.assert_that_element_is_selected(self.CHEKBOX)

    @allure.step("instagram click")
    def click_inst(self):
        self.click(self.INSTAGRAM)

    @allure.step("banner with ventilyator click")
    def click_banner(self):
        self.click(self.VENT_BANNER)

    @allure.step("ventilyator click")
    def vent_click(self):
        self.click(self.VENT)

    @allure.step("add ventilyator to busket")
    def busket_click(self):
        self.click(self.GO_TO_BUSKET)

    @allure.step("enter 10 in the number of ventilyator field")
    def count_input(self):
        self.fill_field(self.VENT_COUNT, '10\n')

    @allure.step("check price of 10 ventilyators")
    def price(self):
        self.assert_that_text_is_displayed(770)

    @allure.step("enter in search")
    def input_in_search(self):
        self.fill_field(self.SEARCH, self.TEXT_FOR_SEARCH)

    @allure.step("is poster visible")
    def image_not_found_is_visible(self):
        self.assert_that_element_is_displayed(self.IMAGE_NOT_FOUND)

    @allure.step("is katalog visible")
    def katalog_visible(self):
        self.assert_that_element_is_displayed(self.KATALOG)

    @allure.step("new click")
    def click_on_element_new(self):
        self.click(self.NEW)

    @allure.step("kitchen click")
    def click_on_element_kitchen(self):
        self.click(self.KITCHEN)

    @allure.step("geo visible check")
    def assert_that_geo_visible(self):
        assert self.get_locator_by_xpath(self.GEO)

    @allure.step("current url check")
    def is_kitchen_url_current(self):
        assert self.current_url(self.KITCHEN_URL)
