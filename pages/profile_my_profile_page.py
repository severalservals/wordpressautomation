from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from random import *

# Profile->My Profile page (url https://wordpress.com/me) is the page served
# when you click the user profile icon in the upper right corner of the Wordpress 
# site and select the top sidebar navigation item (My Profile)
class ProfileMyProfilePageLocator(object):
    DISPLAY_NAME_INPUT = (By.ID, 'display_name')
    SAVE_CHANGES_BUTTON = (By.CSS_SELECTOR, 'p.profile__submit-button-wrapper button[type="submit"]')
    DISABLED_SAVE_CHANGES_BUTTON = (By.CSS_SELECTOR, 'p.profile__submit-button-wrapper button[type="submit"][disabled]')
    SETTINGS_CHANGED_ALERT = (By.CSS_SELECTOR, '#notices span.notice__text')

class ProfileMyProfilePage(Browser):
    # If no value for displayNameValue is given, method will generate a random alpha display name 5-20 characters long.
    # Return value is the value set for the display name - only useful if a random display name was used.
    def setDisplayName(self, displayNameValue = ''):
        if displayNameValue == '':
            displayNameValue = self.randomAlphaString(5, 20)
        # Select all existing text so it is overwritten when new text is set
        self.driver.find_element(*ProfileMyProfilePageLocator.DISPLAY_NAME_INPUT).send_keys(Keys.CONTROL + 'A')
        self.driver.find_element(*ProfileMyProfilePageLocator.DISPLAY_NAME_INPUT).send_keys(displayNameValue)
        return displayNameValue

    def getDisplayName(self):
        return self.driver.find_element(*ProfileMyProfilePageLocator.DISPLAY_NAME_INPUT).value

    def saveChanges(self):
        self.driver.find_element(*ProfileMyProfilePageLocator.SAVE_CHANGES_BUTTON).click()
        # Wait for the successful save message to pop up. That will tell you that edited properties like display name
        # should also have updated on the page.
        # This is a neat looking solution to figuring out whether or not the display name has updated, but 
        # it might not turn out to be the most reliable. If the timing of the alert window isn't exactly synced to
        # the timing of the display name text update, the test will be flaky. If that happens, a clunkier but 
        # more reliable alternative would be navigating to another tab like Account Settings, navigating back and 
        # then checking display name.  
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(ProfileMyProfilePageLocator.SETTINGS_CHANGED_ALERT))

    # This is a generally useful method I'd pull out into a base class or a utility class in a real project. 
    def randomAlphaString(self, minlength, maxlength):
        letters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        rndStr = ''
        numChars = randint(minlength, maxlength)
        for x in range(numChars - 1):
            letterIdx = randint(0, 26)
            rndStr = rndStr + letters[letterIdx]
        return rndStr
