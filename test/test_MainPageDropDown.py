from selenium import webdriver
from PageObject.MainPageDropDown import MainPageDropDown
from PageObject.Texts import TextInfo

class TestQuestionsAndAnswers():

    def test_first_question(self, driver):
        number_question = 1
        main_page = MainPageDropDown()
        main_page.click_cookie_button()
        main_page.scroll_to_the_bottom_main_page()
        assert main_page.get_question_btn_text(number_question) == TextInfo.QUESTIONS_TEXT[number_question]
        main_page.click_question_btn(number_question)
        assert main_page.get_answer_btn_text(number_question) == TextInfo.ANSWERS_TEXT[number_question]

