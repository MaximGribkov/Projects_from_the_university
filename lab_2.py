import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Lab2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_number(self):
        self.driver.get('https://psychicscience.org/random')
        # Считываем парамерты
        first = self.driver.find_element(By.ID, 'num')
        second = self.driver.find_element(By.ID, 'st')
        third = self.driver.find_element(By.ID, 'en')
        choose = self.driver.find_element(By.ID, 'rpt')
        button = self.driver.find_element(By.ID, 'go')
        # Вводим значения
        first_label = int(input('Enter num of numbers: '))
        from_number = int(input('Enter a number from: '))
        to_number = int(input('Enter a number to: '))
        options = int(input('1 - Open Sequnce, 2 - Closed Sequence, 3 - Unique Values: \n'))
        first.send_keys(first_label)
        second.send_keys(from_number)
        third.send_keys(to_number)
        if options == 1:
            choose.send_keys('Open Sequence')
        elif options == 2:
            choose.send_keys('Closed Sequence')
        elif options == 3:
            choose.send_keys('Unique Values')
        else:
            self.fail('Please choose either 1 or 2 or 3')

        button.click()
        time.sleep(5)
        # Вывод ответа
        output = self.driver.find_element(
            By.ID, 'output').get_attribute('value')
        if not output:
            error = self.driver.find_element(By.ID, 'Messages').text
            self.fail(error)

        print('Random num: {}'.format(output))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
