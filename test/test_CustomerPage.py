from PageObject.MainPageDropDown import MainPageDropDown
from PageObject.CustomerPage import CustomerPage
from PageObject.RentPage import RentPage
import time
import allure

from test.config import TestData


class TestCustomerRent:

    @allure.title('Проходим сценарий заказа через хедер')
    def test_order_from_header_success(self, driver):
        main_page = MainPageDropDown(driver)
        customer_page = CustomerPage(driver)
        rent_page = RentPage(driver)
        main_page.click_cookie_button()
        main_page.click_order_button_header()
        customer_page.send_data_about_customer(
            TestData.DATA_FOR_FIRST_ORDER['name'],
            TestData.DATA_FOR_FIRST_ORDER['lastname'],
            TestData.DATA_FOR_FIRST_ORDER['address'],
            TestData.DATA_FOR_FIRST_ORDER['subway_station'],
            TestData.DATA_FOR_FIRST_ORDER['phone']
        )
        customer_page.click_continue_button()

        rent_page.send_data_about_rent(
            TestData.DATA_FOR_FIRST_ORDER['date'],
            TestData.DATA_FOR_FIRST_ORDER['duration_rent'],
            TestData.DATA_FOR_FIRST_ORDER['color'],
            TestData.DATA_FOR_FIRST_ORDER['comment']
        )
        rent_page.click_button_submit()
        rent_page.click_popup_button_confirm()
        time.sleep(1)
        rent_page.click_look_status_button()

        main_page.click_logo_yandex_scooter()
        assert main_page.get_url('praktikum') == TestData.BASE_URL
        main_page.click_logo_yandex(1)
        assert main_page.get_url('yandex') == TestData.YANDEX_URL

    @allure.title('Проходим сценарий заказа через блок Как это работает')
    def test_order_from_middle_section(self, driver):
        main_page = MainPageDropDown(driver)
        customer_page = CustomerPage(driver)
        rent_page = RentPage(driver)
        main_page.click_cookie_button()
        main_page.scroll_to_the_bottom_main_page()
        main_page.click_order_button_middle()
        customer_page.send_data_about_customer(
            TestData.DATA_FOR_SECOND_ORDER['name'],
            TestData.DATA_FOR_SECOND_ORDER['lastname'],
            TestData.DATA_FOR_SECOND_ORDER['address'],
            TestData.DATA_FOR_SECOND_ORDER['subway_station'],
            TestData.DATA_FOR_SECOND_ORDER['phone']
        )
        customer_page.click_continue_button()

        rent_page.send_data_about_rent(
            TestData.DATA_FOR_SECOND_ORDER['date'],
            TestData.DATA_FOR_SECOND_ORDER['duration_rent'],
            TestData.DATA_FOR_SECOND_ORDER['color'],
            TestData.DATA_FOR_SECOND_ORDER['comment']
        )
        rent_page.click_button_submit()
        rent_page.click_popup_button_confirm()
        time.sleep(1)
        rent_page.click_look_status_button()

        main_page.click_logo_yandex_scooter()
        assert main_page.get_url('praktikum') == TestData.BASE_URL
        main_page.click_logo_yandex(2)
        assert main_page.get_url('yandex') == TestData.YANDEX_URL








