import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://qa-scooter.praktikum-services.ru/")
driver.maximize_window()

#COOKIE BUTTON
driver.find_element(By.ID, 'rcc-confirm-button').click()
# element = driver.find_element(By.ID, 'accordion__heading-7')
# driver.execute_script("arguments[0].scrollIntoView();", element)
# WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "card__image")))
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.find_element(By.ID, 'accordion__heading-0').click()
time.sleep(2)
text1 = driver.find_element(By.XPATH, '//*[@id="accordion__heading-0"]').text
print(text1)
text = driver.find_element(By.XPATH, '//*[@id="accordion__panel-0"]/p').text
print(text)

# driver.find_element(By.XPATH, ".//form[@name='edit-avatar']/button[text()='Сохранить']").click()

driver.quit()


# ACCORDION0 = [By.ID, 'accordion__heading-0']
#     ACCORDION1 = [By.ID, 'accordion__heading-1']
#     ACCORDION2 = [By.ID, 'accordion__heading-2']
#     ACCORDION3 = [By.ID, 'accordion__heading-3']
#     ACCORDION4 = [By.ID, 'accordion__heading-4']
#     ACCORDION5 = [By.ID, 'accordion__heading-5']
#     ACCORDION6 = [By.ID, 'accordion__heading-6']
#     ACCORDION7 = [By.ID, 'accordion__heading-7']
#     COOKIE_BTN = [By.ID, 'rcc-confirm-button']
#
#     ACCORDION_QUESTION0 = [By.XPATH, '//*[@id="accordion__heading-0"]']
#     ACCORDION_QUESTION1 = [By.XPATH, '//*[@id="accordion__heading-1"]']
#     ACCORDION_QUESTION2 = [By.XPATH, '//*[@id="accordion__heading-2"]']
#     ACCORDION_QUESTION3 = [By.XPATH, '//*[@id="accordion__heading-3"]']
#     ACCORDION_QUESTION4 = [By.XPATH, '//*[@id="accordion__heading-4"]']
#     ACCORDION_QUESTION5 = [By.XPATH, '//*[@id="accordion__heading-5"]']
#     ACCORDION_QUESTION6 = [By.XPATH, '//*[@id="accordion__heading-6"]']
#     ACCORDION_QUESTION7 = [By.XPATH, '//*[@id="accordion__heading-7"]']
#
#     ACCORDION_ANSWER0 = [By.XPATH, '//*[@id="accordion__panel-0"]/p']
#     ACCORDION_ANSWER1 = [By.XPATH, '//*[@id="accordion__panel-1"]/p']
#     ACCORDION_ANSWER2 = [By.XPATH, '//*[@id="accordion__panel-2"]/p']
#     ACCORDION_ANSWER3 = [By.XPATH, '//*[@id="accordion__panel-3"]/p']
#     ACCORDION_ANSWER4 = [By.XPATH, '//*[@id="accordion__panel-4"]/p']
#     ACCORDION_ANSWER5 = [By.XPATH, '//*[@id="accordion__panel-5"]/p']
#     ACCORDION_ANSWER6 = [By.XPATH, '//*[@id="accordion__panel-6"]/p']
#     ACCORDION_ANSWER7 = [By.XPATH, '//*[@id="accordion__panel-7"]/p']
#
#     questions_and_answers_list = {}
#
#     def __init__(self, driver, questions_and_answers_list):
#         super().__init__(driver)
#         self.questions_and_answers_list = questions_and_answers_list
#         self.driver.get(TestData.BASE_URL)
#
#     def click_cookie_button(self):
#         self.do_click(self.COOKIE_BTN)
#
#     def scroll_to_the_bottom_main_page(self):
#         self.scroll_to_the_bottom()
#
#     def checks_zero_accordion(self):
#         self.do_click(self.ACCORDION0)
#         question_text = self.get_element_text(self.ACCORDION_QUESTION0)
#         answer_text_from_page = self.get_element_text(self.ACCORDION_ANSWER0)
#         expected_answer = self.questions_and_answers_list[question_text]
#         return answer_text_from_page == expected_answer