from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# The Login page (url https://wordpress.com/log-in?redirect...) is served when you click Log In on the Public Home page. 
class LoginPageLocator(object):
    USERNAME_FIELD = (By.ID, 'usernameOrEmail')
    PASSWORD_FIELD = (By.ID, 'password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type=''Submit'']')
    # This is a value that's actually on the authenticated page you arrive at after logging in, not the login page. 
    # The Login method uses it to make sure login was successful and that timing is all synced up. 
    AUTHENTICATED_FIELD = (By.CSS_SELECTOR, 'ul.sidebar span[data-e2e-sidebar="My Home"]')

class LoginPage(Browser):
    def login(self, username, password):
        self.driver.find_element(*LoginPageLocator.USERNAME_FIELD).send_keys(username)
        self.click_element(*LoginPageLocator.SUBMIT_BUTTON)
        self.driver.find_element(*LoginPageLocator.PASSWORD_FIELD).send_keys(password)
        self.click_element(*LoginPageLocator.SUBMIT_BUTTON)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(LoginPageLocator.AUTHENTICATED_FIELD))

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()