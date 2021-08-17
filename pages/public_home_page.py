from selenium.webdriver.common.by import By
from browser import Browser

# Public Home Page is the unauthenticated landing page served by default at https://wordpress.com

class PublicHomePageLocator(object):
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a[title="Log In"]')

class PublicHomePage(Browser):
    # Home Page Actions
    def navigate(self, address):
        self.driver.get(address)
        
    def go_to_login(self):
        self.click_element(*PublicHomePageLocator.LOGIN_BUTTON)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

