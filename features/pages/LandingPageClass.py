import time

from selenium.webdriver.common.by import By


class LandingPageClass:

    def __init__(self, driver):
        self.driver = driver

        # Element Locators Values
        self.loginicon = "//a[@data-clicktext='Login']"
        self.mobiletextbox = "//input[@inputmode='numeric']"
        self.pintextbox = "//input[@id='pb-pin-number']"
        self.frameElement = "//iframe[@name='a-kfulw02w6ea7']"
        self.checkBoxElement = "//div[@class='recaptcha-checkbox-border']"
        self.loginbutton = "//button[@class='btn pb-login-submit red-button']"
        self.paybackelement = "//a[@class='nav-link']"
        self.emailbox="//input[@name='email']"
        self.mobilebox="//input[@name='user_mobile_number']"
        self.confirmbutton="//button[@id='redeemBtn']"

# Creating Element Methods
    def click_login_icon(self):
        loginicon = self.driver.find_element(By.XPATH, self.loginicon)
        loginicon.click()

    def enter_mobile_textbox(self, mn):
        mobiletextbox = self.driver.find_element(By.XPATH, self.mobiletextbox)
        mobiletextbox.send_keys(mn)

    def enter_pin_textbox(self,mn):
      pintextbox = self.driver.find_element(By.XPATH, self.pintextbox)
      pintextbox.send_keys(mn)

    def select_check_box(self):
        frameField = self.driver.find_element(By.TAG_NAME, self.frameElement)
        self.driver.switch_to.frame(frameField)
        checkBoxField = self.driver.find_element(By.XPATH, self.checkBoxElement)
        checkBoxField.click()
        time.sleep(20)
        self.driver.switch_to.default_content()


    def click_login_button(self):
          loginbutton = self.driver.find_element(By.XPATH, self.loginbutton)
          loginbutton.click()

    def click_payback_element(self):
        paybackelement = self.driver.find_element(By.XPATH, self.paybackelement)
        paybackelement.click()

    def enter_emailbox(self,em):
        emailbox = self.driver.find_element(By.XPATH, self.emailbox)
        emailbox.click()
        emailbox.clear()
        emailbox.send_keys(em)


    def enter_mobilebox(self,mn):
        mobilebox = self.driver.find_element(By.XPATH, self.mobilebox)
        mobilebox.send_keys(mn)


    def click_confirmbutton(self):
            confirmbutton = self.driver.find_element(By.XPATH, self.confirmbutton)
            confirmbutton.click()


