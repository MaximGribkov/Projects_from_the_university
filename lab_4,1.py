import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Lab_04(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_blog(self):
        self.driver.get('https://habr.com/ru/all/')

        number_of_posts = self.driver.find_elements(
            By.CLASS_NAME, 'tm-article-snippet__title-link')

       # пробегаемся по списку постов, открываем их и возращаемся обратно
       # так делаем 3 раза по заданию
        for i in range(len(number_of_posts)):
            if (i > 2):
                break

            number_of_posts[i].click()
            time.sleep(2)

            self.driver.back()
            time.sleep(2)

            self.driver.implicitly_wait(3)

            number_of_posts = self.driver.find_elements(
                By.CLASS_NAME, 'tm-article-snippet__title-link')

        # находим элемент пагинации и спускаемся до него
        pagination = self.driver.find_elements(
            By.CLASS_NAME, 'tm-pagination__page')
        pagination[0].location_once_scrolled_into_view

        time.sleep(2)

        # пробегаемся по элементам пагинации и открываем их
        for i in range(len(pagination)):
            if (i > 3):
                break

            pagination[i].click()

            time.sleep(1)

            self.driver.implicitly_wait(3)
            pagination = self.driver.find_elements(
                By.CLASS_NAME, 'tm-pagination__page')

        # выводим количество постов на главной странице
        print('Number of posts: ', len(number_of_posts))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
