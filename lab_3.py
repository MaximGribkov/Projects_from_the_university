import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Lab3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_find_testcase(self):
        self.driver.get('https://google.com')
        input_ = self.driver.find_element(By.TAG_NAME, 'input')
        # Вводим в поиске
        input_.send_keys('testcase')
        input_.send_keys(Keys.ENTER)
        time.sleep(1)
        # Открываем первую страницу
        link = self.driver.find_element(
            By.XPATH, '//*[contains(text(), "Test Case")]')
        link.click()
        # Ведем подсчет совпадений
        test_case = self.driver.find_elements(
            By.XPATH, '//*[contains(text(), "testcase")]')
        test = self.driver.find_elements(
            By.XPATH, '//*[contains(text(), "test")]')
        case = self.driver.find_elements(
            By.XPATH, '//*[contains(text(), "case")]')
        time.sleep(1)
        # Вывод результатов
        print(' TestCase: {0}\n test:{1}\n case: {2}\n'
              .format(len(test_case), len(test), len(case)))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
