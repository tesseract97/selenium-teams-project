import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from chromedriver_py import binary_path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#instance of webdriver is created


class LogIn:
    def __init__(self, email, password):

        self.driver = webdriver.Chrome(executable_path=binary_path)
        self.driver.get("http://teams.microsoft.com")
        self.wait_for_credentials("loginfmt", email)
        #Password
        self.wait_for_credentials("Password", password)
        self.stay_logged_in("idBtn_Back")
        self.web_app("a[ng-click='$ctrl.useWeb()']")
        time.sleep(20)

        self.driver.close()



    def wait_for_credentials(self, locator, input):
        try:
            elem_present = EC.presence_of_element_located((By.NAME, locator))
            WebDriverWait(self.driver, 10).until(elem_present)
            username = self.driver.find_element_by_name(locator)
            username.send_keys(input)
            username.send_keys(Keys.RETURN)
        except TimeoutException:
            ("Timed_Out")

    def stay_logged_in(self, locator):
        try:
            elem_present = EC.presence_of_element_located((By.ID, locator))
            WebDriverWait(self.driver, 10).until(elem_present)
            no_button = self.driver.find_element_by_id(locator)
            no_button.submit()
        except TimeoutException:
            print("TimeOut 1")

    def web_app(self, locator):

        try:
            elem_present = EC.presence_of_element_located((By.CSS_SELECTOR, locator))
            WebDriverWait(self.driver, 10).until(elem_present)
            web_app = self.driver.find_element_by_css_selector(locator)
            web_app.click()
        except TimeoutException:
            print("TimeOut2")


#go to chat
#join call
#join or accept buttons

if __name__ == "__main__":
    LogIn("tessa.condon@mail.mcgill.ca", "jackie03")