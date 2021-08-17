from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Navbars page is not a page in itself - it's a container for the top and side
# navigation bars displayed on the Wordpress profile pages.  
class NavbarsPageLocator(object):
    PROFILE_BUTTON = (By.CSS_SELECTOR, '#header a[href="/me"] img[alt="My Profile"]')
    # ul.sidebar h2.profile-gravatar__user-display-name
    DISPLAY_NAME_NODE = (By.CSS_SELECTOR, 'ul.sidebar h2.profile-gravatar__user-display-name')

class NavbarsPage(Browser):
    def profileButtonIsPresent(self):
        return self.driver.find_element(*NavbarsPageLocator.PROFILE_BUTTON)

    def getDisplayNameText(self):
        return self.driver.find_element(*NavbarsPageLocator.DISPLAY_NAME_NODE).text
    
    def clickProfileButton(self): 
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(NavbarsPageLocator.PROFILE_BUTTON))
        element.click()