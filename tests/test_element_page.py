import allure

from page.ElementPage import ElementPage


@allure.title("katalog visible check")
def test_katalog_visible(browser_chrome, open_page):
    element = ElementPage(browser_chrome)

    element.katalog_visible()


@allure.title("new visible check")
def test_click_new(browser_chrome, open_page):
    element = ElementPage(browser_chrome)

    element.click_on_element_new()


@allure.title("current url check")
def test_click_kitchen(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_on_element_kitchen()
    element.is_kitchen_url_current()


@allure.title("check for invalid request")
def test_incorrect_search(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.input_in_search()
    element.image_not_found_is_visible()


@allure.title("adding a product and checking the price")
def test_ventilyator(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_banner()
    element.vent_click()
    element.busket_click()
    element.count_input()
    element.price()


@allure.title("link to instagram")
def test_instagram(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_inst()


@allure.title("checkbox validation")
def test_action(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_action()
    element.click_chekbox()
    element.select_checkbox()


@allure.title("is poster visible check")
def test_katalog(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_katalog()
    element.installment()
    element.poster()


@allure.title("pop-up window on click like")
def test_like(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_like()
    element.drop_like()


@allure.title("pop-up window on click compare")
def test_compare(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_compare()
    element.drop_compare()


@allure.title("incorrect data user entry")
def test_user_email(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_user()
    element.login()
    element.password()
    element.click_entry()
    element.user_not_found()


@allure.title("login with viber")
def test_user_viber(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_user()
    element.viber_entry()
    element.mobile_num()
    element.sms_button()
    element.code()


@allure.title("incorrectly entered code")
def test_user_viber_code(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_user()
    element.viber_entry()
    element.mobile_num()
    element.sms_button()
    element.code()
    element.inter_code()
    element.entry_code()
    element.invalid_code()


@allure.title("login with vk displayed")
def test_user_vk_display(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_user()
    element.user_vk()


@allure.title("login with google displayed")
def test_user_google_display(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_user()
    element.user_google()


@allure.title("login with yandex displayed")
def test_user_yandex_display(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_user()
    element.user_yandex()


@allure.title("login with facebook displayed")
def test_user_facebook_display(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_user()
    element.user_facebook()


@allure.title("login with vk click")
def test_user_vk_click(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_user()
    element.user_vk_click()


@allure.title("login with google click")
def test_user_google_click(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_user()
    element.user_google_click()


@allure.title("login with yandex click")
def test_user_yandex_click(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_user()
    element.user_yandex_click()


@allure.title("login with facebook click")
def test_user_facebook_click(browser_chrome, open_page):
    element = ElementPage(browser_chrome)
    element.click_user()
    element.user_facebook_click()
