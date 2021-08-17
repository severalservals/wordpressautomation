from browser import Browser
from selenium import webdriver
from pages.navbars_page import NavbarsPage
from pages.public_home_page import PublicHomePage
from pages.login_page import LoginPage
from pages.profile_my_profile_page import ProfileMyProfilePage

def selenium_browser_chrome(context):
    context.browser = webdriver.Chrome()
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()
    yield context.browser
    context.browser.quit()

def before_all(context):
    context.config.setup_logging()
    context.browser = Browser()
    context.navbars_page = NavbarsPage()
    context.public_home_page = PublicHomePage()
    context.login_page = LoginPage()
    context.profile_my_profile_page = ProfileMyProfilePage()
    # The values below are the username and password the automated tests will use to get in 
    # to the application. We do always want them to work so they aren't test data and we 
    # wouldn't put them in a table. We do want them in one easily located place. 
    # Conceptually they're environment variables. 
    context.tests_username = 'severalservals'
    context.tests_password = 'dK5RbZa82bcwDL8'

def after_all(context):
    context.browser.close()
