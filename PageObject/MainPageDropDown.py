from PageObject.BasePage import BasePage
from selenium.webdriver.common.by import By
from test.config import TestData

class MainPageDropDown(BasePage):

    questions = {
        1: [By.ID, 'accordion__heading-0'],
        2: [By.ID, 'accordion__heading-1'],
        3: [By.ID, 'accordion__heading-2'],
        4: [By.ID, 'accordion__heading-3'],
        5: [By.ID, 'accordion__heading-4'],
        6: [By.ID, 'accordion__heading-5'],
        7: [By.ID, 'accordion__heading-6'],
        8: [By.ID, 'accordion__heading-7']
    }

    answers = {
        1: [By.ID, 'accordion__panel-0'],
        2: [By.ID, 'accordion__panel-1'],
        3: [By.ID, 'accordion__panel-2'],
        4: [By.ID, 'accordion__panel-3'],
        5: [By.ID, 'accordion__panel-4'],
        6: [By.ID, 'accordion__panel-5'],
        7: [By.ID, 'accordion__panel-6'],
        8: [By.ID, 'accordion__panel-7'],
    }

    COOKIE_BTN = [By.ID, 'rcc-confirm-button']

    def __init__(self, driver):
        super().__init__(driver)

    def click_cookie_button(self):
        self.do_click(self.COOKIE_BTN)

    def scroll_to_the_bottom_main_page(self):
        self.scroll_to_the_bottom()

    def click_question_btn(self, number_btn):
        self.do_click(self.questions[number_btn])

    def get_question_btn_text(self, number_btn):
        self.get_element_text(self.questions[number_btn])

    def get_answer_btn_text(self, number_btn):
        self.get_element_text(self.answers[number_btn])




