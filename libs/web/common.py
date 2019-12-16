from selenium.webdriver.common.by import By


class JobListing(object):
    def __init__(self, conatiner):
        self.container = conatiner

    @property
    def title(self):
        return self.container.find_element(By.CSS_SELECTOR, "span.job-title").text

    @property
    def type(self):
        return self.container.find_element(By.CSS_SELECTOR, "div.job-type").text

    @property
    def location(self):
        return self.container.find_element(By.CSS_SELECTOR, "div.job-location").text

    @property
    def date(self):
        return self.container.find_element(By.CSS_SELECTOR, "div.job-date").text

    @property
    def description(self):
        return self.container.find_element(By.CSS_SELECTOR, "div.job-description").text

    @property
    def button_read_more(self):
        return self.container.find_element(By.CSS_SELECTOR, "a.btn btn-primary")
