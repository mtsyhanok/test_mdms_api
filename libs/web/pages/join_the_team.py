from selenium.webdriver.common.by import By

from libs.web.base_page import BasePage
from libs.web.common import JobListing
from settings import HEALTH_BRIDGE_HOST


JOIN_THE_TEAM_URL = '/join-the-team'
JOIN_THE_TEAM_TITLE = 'My HealthBridge | Join The Team'


class JoinTheTeam(BasePage):
    def __init__(self):
        super(JoinTheTeam, self).__init__()
        self.url = HEALTH_BRIDGE_HOST + JOIN_THE_TEAM_URL
        self.title = JOIN_THE_TEAM_TITLE

    @property
    def input_keywords(self):
        keywords = self.driver.find_element(By.ID, "keywords")
        keywords.clear()
        return keywords

    @property
    def select_category(self):
        return self.driver.find_element(By.ID, "category")

    @property
    def select_job_type(self):
        return self.driver.find_elements(By.ID, "jobtype")

    @property
    def select_location(self):
        return self.driver.find_element(By.ID, "cart-location")

    @property
    def button_search(self):
        return self.driver.find_element(By.XPATH, "//input[@type='submit']")

    @property
    def jobs_list(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.list-view")

    @property
    def jobs_listings(self):
        jobs = self.driver.find_elements(By.CSS_SELECTOR, "div.list-data")
        return [JobListing(job) for job in jobs]
