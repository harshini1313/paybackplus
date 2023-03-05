import time
from hamcrest import *
from behave import *

from features.pages.LandingPageClass import LandingPageClass


@when("user cliks on login icon")
def step_impl(context):
    time.sleep(2)
    landingPage = LandingPageClass(context.driver)
    landingPage.click_login_icon()

@step('user enters mobile number "{mobile}"')
def step_impl(context,mobile):
 time.sleep(2)
 landingPage = LandingPageClass(context.driver)
 landingPage.enter_mobile_textbox(mobile)

 @step('user enters pin "{pin}"')
 def step_impl(context,pin):
     time.sleep(2)
     landingPage = LandingPageClass(context.driver)
     landingPage.enter_pin_textbox(pin)


@when("User selects Check Box on reCAPTCHA")
def step_impl(context):
    landingPage = LandingPageClass(context.driver)
    landingPage.select_check_box()

@then("user clicks on login button")
def step_impl(context):
    time.sleep(2)
    landingPage = LandingPageClass(context.driver)
    landingPage.click_login_button()

@given("Chrome is opened and Payback app is opened")
def step_impl(context):
    time.sleep(5)
    expectedTitle = "Largest Multi-brand Loyalty Program in India - PAYBACK"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
    time.sleep(5)


@when("User clicks on join payback plus button")
def step_impl(context):
    landingpage = LandingPageClass(context.driver)
    landingpage.click_payback_element()

@then("It shows payback plus page")
def step_impl(context):
    time.sleep(5)
    expectedTitle = "paybackplus"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
    time.sleep(5)
'''
@step("user removes the default email Id")
def step_impl(context):
    pass
    '''

@then('User enters email Id "{email}"')
def step_impl(context,email):
    time.sleep(5)
    landingPage = LandingPageClass(context.driver)
    landingPage.enter_emailbox(email)

'''
@step("user removes the default mobile number")
def step_impl(context):
        clearbox=LandingPageClass(context.driver)
        clearbox.enter_emailbox()
        '''

@step('user enters mobile number"{mobile}"')
def step_impl(context,mobile):
    time.sleep(3)
    landingPage = LandingPageClass(context.driver)
    landingPage.enter_mobilebox(mobile)

@then("user clicks the confirm button")
def step_impl(context):
    time.sleep(2)
    landingPage = LandingPageClass(context.driver)
    landingPage.click_confirmbutton()


@step('User enters invalid invalid email Id {"email"}')
def step_impl(context,email):
    time.sleep(5)
    landingPage = LandingPageClass(context.driver)
    landingPage.enter_emailbox(email)