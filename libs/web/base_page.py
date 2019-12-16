from hamcrest import assert_that, equal_to
from selenium import webdriver

from settings import WEBDRIVER_PATH


class BasePage(object):
    def __init__(self):
        self.driver = webdriver.Chrome(WEBDRIVER_PATH)
        self.url = ''

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.close()

    def check_title(self, title):
        assert_that(self.driver.title, equal_to(title),
                    'Incorrect title: {0}. Expected: {1}'.format(self.driver.title, title))
