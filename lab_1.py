import unittest
from selenium import webdriver
import random
import time


class Lab1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_open_and_close_links(self):
        links = []
        # читаем ссылки из текстового файла
        with open('links.txt', 'r') as f:
            for link in f:
                links.append(link)
        print('Links: {}'.format(links))

        # перемешиваем ссылки
        random.shuffle(links)
        print('Updated links: {}'.format(links))

        # пробегаемся по списку ссыллок и открываем каждую в новой вкладке
        for i in range(len(links)):
            self.driver.get(links[i])
            if i == 9:
                break
            self.driver.execute_script("window.open('');")
            self.driver.switch_to.window(self.driver.window_handles[i + 1])

        time.sleep(5)

        t = len(links) - 1

        # закрываем ссылки в обратной последовательности
        for i in range(len(links)):
            self.driver.switch_to.window(self.driver.window_handles[t])
            self.driver.close()
            t -= 1
            time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
