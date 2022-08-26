from PageObject.MainPageDropDown import MainPageDropDown
from PageObject.Texts import TextInfo
import time
import allure


class TestMainPageDropDown:

    @allure.title('Проверка вопроса №1')
    def test_first_question(self, driver):
        number_question = 1
        main_page = MainPageDropDown(driver)
        main_page.click_cookie_button()
        main_page.scroll_to_the_bottom_main_page()
        main_page.click_question_btn(number_question)
        time.sleep(2)
        assert main_page.get_question_btn_text(number_question) == TextInfo.QUESTIONS_TEXT[number_question] \
               and main_page.get_answer_btn_text(number_question) == TextInfo.ANSWERS_TEXT[number_question]

    @allure.title('Проверка вопроса №2')
    def test_second_question(self, driver):
        number_question = 2
        main_page = MainPageDropDown(driver)
        main_page.click_cookie_button()
        main_page.scroll_to_the_bottom_main_page()
        main_page.click_question_btn(number_question)
        time.sleep(2)
        assert main_page.get_question_btn_text(number_question) == TextInfo.QUESTIONS_TEXT[number_question] \
               and main_page.get_answer_btn_text(number_question) == TextInfo.ANSWERS_TEXT[number_question]

    @allure.title('Проверка вопроса №3')
    def test_second_question(self, driver):
        number_question = 3
        main_page = MainPageDropDown(driver)
        main_page.click_cookie_button()
        main_page.scroll_to_the_bottom_main_page()
        main_page.click_question_btn(number_question)
        time.sleep(2)
        assert main_page.get_question_btn_text(number_question) == TextInfo.QUESTIONS_TEXT[number_question] \
               and main_page.get_answer_btn_text(number_question) == TextInfo.ANSWERS_TEXT[number_question]

    @allure.title('Проверка вопроса №4')
    def test_second_question(self, driver):
        number_question = 4
        main_page = MainPageDropDown(driver)
        main_page.click_cookie_button()
        main_page.scroll_to_the_bottom_main_page()
        main_page.click_question_btn(number_question)
        time.sleep(2)
        assert main_page.get_question_btn_text(number_question) == TextInfo.QUESTIONS_TEXT[number_question] \
               and main_page.get_answer_btn_text(number_question) == TextInfo.ANSWERS_TEXT[number_question]

    @allure.title('Проверка вопроса №5')
    def test_first_question(self, driver):
        number_question = 5
        main_page = MainPageDropDown(driver)
        main_page.click_cookie_button()
        main_page.scroll_to_the_bottom_main_page()
        main_page.click_question_btn(number_question)
        time.sleep(2)
        assert main_page.get_question_btn_text(number_question) == TextInfo.QUESTIONS_TEXT[number_question] \
               and main_page.get_answer_btn_text(number_question) == TextInfo.ANSWERS_TEXT[number_question]

    @allure.title('Проверка вопроса №6')
    def test_second_question(self, driver):
        number_question = 6
        main_page = MainPageDropDown(driver)
        main_page.click_cookie_button()
        main_page.scroll_to_the_bottom_main_page()
        main_page.click_question_btn(number_question)
        time.sleep(2)
        assert main_page.get_question_btn_text(number_question) == TextInfo.QUESTIONS_TEXT[number_question] \
               and main_page.get_answer_btn_text(number_question) == TextInfo.ANSWERS_TEXT[number_question]

    @allure.title('Проверка вопроса №7')
    def test_second_question(self, driver):
        number_question = 7
        main_page = MainPageDropDown(driver)
        main_page.click_cookie_button()
        main_page.scroll_to_the_bottom_main_page()
        main_page.click_question_btn(number_question)
        time.sleep(2)
        assert main_page.get_question_btn_text(number_question) == TextInfo.QUESTIONS_TEXT[number_question] \
               and main_page.get_answer_btn_text(number_question) == TextInfo.ANSWERS_TEXT[number_question]

    @allure.title('Проверка вопроса №8')
    def test_second_question(self, driver):
        number_question = 8
        main_page = MainPageDropDown(driver)
        main_page.click_cookie_button()
        main_page.scroll_to_the_bottom_main_page()
        main_page.click_question_btn(number_question)
        time.sleep(2)
        assert main_page.get_question_btn_text(number_question) == TextInfo.QUESTIONS_TEXT[number_question] \
               and main_page.get_answer_btn_text(number_question) == TextInfo.ANSWERS_TEXT[number_question]
