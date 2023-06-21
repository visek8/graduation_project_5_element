import allure

from page.ShopsPage import ShopsPage


@allure.title("shop_1 display check")
def test_shop_1_visible(browser_chrome, open_shops_page):
    element = ShopsPage(browser_chrome)
    element.shop_1_displ()


@allure.title("shop_2 display check")
def test_shop_2_visible(browser_chrome, open_shops_page):
    element = ShopsPage(browser_chrome)
    element.shop_2_displ()


@allure.title("shop_3 display check")
def test_shop_3_visible(browser_chrome, open_shops_page):
    element = ShopsPage(browser_chrome)
    element.shop_3_displ()


@allure.title("shop_4 display check")
def test_shop_4_visible(browser_chrome, open_shops_page):
    element = ShopsPage(browser_chrome)
    element.shop_4_displ()


@allure.title("map_1 display check")
def test_shop_1_map(browser_chrome, open_shops_page):
    element = ShopsPage(browser_chrome)
    element.shop_1_click()
    element.shops_map_displ()


@allure.title("map_2 display check")
def test_shop_2_map(browser_chrome, open_shops_page):
    element = ShopsPage(browser_chrome)
    element.shop_2_click()
    element.shops_map_displ()


@allure.title("shop in Brest display check")
def test_city_brest(browser_chrome, open_shops_page):
    element = ShopsPage(browser_chrome)
    element.click_city()
    element.click_brest()
    element.shop_brest_visib()


@allure.title("shop in Grodno display check")
def test_city_grodno(browser_chrome, open_shops_page):
    element = ShopsPage(browser_chrome)
    element.click_city()
    element.click_grodno()
    element.shop_grodno_visib()


@allure.title("shop in Baranovichi display check")
def test_city_baranovichi(browser_chrome, open_shops_page):
    element = ShopsPage(browser_chrome)
    element.click_city()
    element.click_baranovichi()
    element.shop_baranovichi_visib()


@allure.title("shop in Bereza display check")
def test_city_bereza(browser_chrome, open_shops_page):
    element = ShopsPage(browser_chrome)
    element.click_city()
    element.click_bereza()
    element.shop_bereza_visib()
