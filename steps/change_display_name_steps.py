from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

# Steps for logging in, navigating to the profile page, updating and verifying the 
@given('I log in to Wordpress and navigate to the profile page')
def step_impl(context):
    context.public_home_page.navigate('https://wordpress.com')
    context.public_home_page.go_to_login()
    context.login_page.login(context.tests_username, context.tests_password)
    context.navbars_page.clickProfileButton()

@when('I change the display name to a new value and save')
def step_impl(context):
    context.newDisplayName = context.profile_my_profile_page.setDisplayName()
    context.profile_my_profile_page.saveChanges()

@then('The new display name should display in the display name field')
def step_impl(context):
    assert_true(context.newDisplayName == context.navbars_page.getDisplayNameText())