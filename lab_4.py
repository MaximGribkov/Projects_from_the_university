import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Lab4(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_blog(self):

        self.driver.get('https://ru.stackoverflow.com/questions')
        number_of_posts = self.driver.find_elements(
            By.CLASS_NAME, 's-post-summary--content-title')

        for i in range(len(number_of_posts)):
            if i > 2:
                break
            number_of_posts[i].click()

            time.sleep(1)

            self.driver.back()

            time.sleep(1)

            self.driver.implicitly_wait(3)
            number_of_posts = self.driver.find_elements(
                By.CLASS_NAME, 's-post-summary--content-title')

        time.sleep(1)
        first_page = self.driver.find_elements(
            By.XPATH, "//div[@class='s-pagination--item is-selected']")
        first_page[0].location_once_scrolled_into_view

        time.sleep(1)

        num_page = self.driver.find_elements(
            By.XPATH, "//a[@class='s-pagination--item js-pagination-item']")

        for i in range(len(num_page)):
            if i > 3:
                break
            else:
                num_page[i].click()
                time.sleep(1)
                self.driver.implicitly_wait(3)
                num_page = self.driver.find_elements(
                    By.XPATH, "//a[@class='s-pagination--item js-pagination-item']")

        print('Number of posts: {}'.format(len(number_of_posts)))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
