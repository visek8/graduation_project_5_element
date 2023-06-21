import allure

from page.BasePage import BasePage


class ShopsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.SHOP_1 = '//*[@alt="Пятый Элемент, ул. Денисовская, 8 (ТЦ  «Корона-Сити», 1 этаж)"]'
        self.SHOP_2 = '//*[@alt="Пятый Элемент, ул. Корженевского, 26 (ТЦ «Корона», 1 этаж)"]'
        self.SHOP_3 = '//*[@alt="Пятый Элемент, пр-т Победителей, 65/1 (ТЦ «Замок», 4 этаж)"]'
        self.SHOP_4 = '//*[@alt="Пятый Элемент, пр-т Независимости, 154 (ТЦ «Корона», 1 этаж)"]'

        self.SHOP_MAP = '//*[@class = "ymaps-2-1-79-events-pane ymaps-2-1-79-user-selection-none"]'

        self.CITY = '//*[@id="shop-list-change-city-btn"]'
        self.BREST = 'Брест'
        self.SHOP_BREST = '//*[@alt="Пятый Элемент, Варшавское шоссе, 11 (ТЦ «Евроопт», 1 этаж)"]'

        self.GRODNO = 'Гродно'
        self.SHOP_GRODNO = '//*[@alt="Пятый Элемент, пр-т Я.Купалы, 87 (ТРК «Тринити», 3 этаж)"]'

        self.BEREZA = 'Берёза'
        self.SHOP_BEREZA = '//*[@alt="Пятый Элемент, ул. Ленина, 101 (ТЦ «Санта»)"]'

        self.BARANOVICHI = 'Барановичи'
        self.SHOP_BARANOVICHI = '//*[@alt="Пятый Элемент, пр-т Советский 2-1"]'

    @allure.step("shop in Baranovichi display check")
    def shop_baranovichi_visib(self):
        self.assert_that_element_is_displayed(self.SHOP_BARANOVICHI)

    @allure.step("select Baranovichi")
    def click_baranovichi(self):
        self.click_text(self.BARANOVICHI)

    @allure.step("shop in Bereza display check")
    def shop_bereza_visib(self):
        self.assert_that_element_is_displayed(self.SHOP_BEREZA)

    @allure.step("select Bereza")
    def click_bereza(self):
        self.click_text(self.BEREZA)

    @allure.step("shop in Grodno display check")
    def shop_grodno_visib(self):
        self.assert_that_element_is_displayed(self.SHOP_GRODNO)

    @allure.step("select Grodno")
    def click_grodno(self):
        self.click_text(self.GRODNO)

    @allure.step("shop in Brest display check")
    def shop_brest_visib(self):
        self.assert_that_element_is_displayed(self.SHOP_BREST)

    @allure.step("select Brest")
    def click_brest(self):
        self.click_text(self.BREST)

    @allure.step("click to city")
    def click_city(self):
        self.click(self.CITY)

    @allure.step("map display check")
    def shops_map_displ(self):
        self.assert_that_element_is_displayed(self.SHOP_MAP)

    @allure.step("shop_1 display check")
    def shop_1_displ(self):
        self.assert_that_element_is_displayed(self.SHOP_1)

    @allure.step("shop_2 display check")
    def shop_2_displ(self):
        self.assert_that_element_is_displayed(self.SHOP_2)

    @allure.step("shop_3 display check")
    def shop_3_displ(self):
        self.assert_that_element_is_displayed(self.SHOP_3)

    @allure.step("shop_4 display check")
    def shop_4_displ(self):
        self.assert_that_element_is_displayed(self.SHOP_4)

    @allure.step("click to shop_1")
    def shop_1_click(self):
        self.click(self.SHOP_1)

    @allure.step("click to shop_2")
    def shop_2_click(self):
        self.click(self.SHOP_2)
