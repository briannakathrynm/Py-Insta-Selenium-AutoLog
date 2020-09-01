from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Login:
    def __init__(self, driver, username, password, backup_code, post_count):
        self.driver = driver
        self.username = username
        self.password = password
        self.backup_code = backup_code
        self.post_count = post_count

    def sign_in(self, expected_url='https://www.instagram.com/accounts/login/two_factor?source=auth_switcher&next=%2F'):

        """
        Function that signs in automatically into Instagram with a specified username and password.
        Note: This function takes into consideration TwoFact Authentication.
        Variables:
        Self: self
        expected_url: URL of Instagram 2F if enabled.
        :return: None, opens an instance of Chrome and automatically logs in.
        """

        print('Signing In...')
        self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        # Looks for username in a specific amount of time, enough for webpage to load
        user_id = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
            '#loginForm > div > div:nth-child(1) > div > label > input')))
        user_id.click()
        user_id.send_keys(self.username)

        # Looks for password in a specific amount of time, enough for webpage to load
        pwd = self.driver.find_element_by_css_selector(
            '#loginForm > div > div:nth-child(2) > div > label > input')
        pwd.click()
        pwd.send_keys(self.password)
        # Clicks on Login Button
        button = self.driver.find_element_by_css_selector(
            '#loginForm > div > div:nth-child(3)')
        button.click()

        # Now checking for 2Fact Authentication...
        time.sleep(3)
        if self.driver.current_url == expected_url:
            print("TwoFact Enabled")
            two_fact = self.driver.find_element_by_css_selector(
                '#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div.gi2oZ > div > label > input')
            two_fact.click()
            two_fact.send_keys(self.backup_code)
            # Clicks on Confirm button
            button = self.driver.find_element_by_css_selector(
                '#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div.Igw0E.IwRSH.eGOV_._4EzTm.MGdpg.CovQj.jKUp7.iHqQ7 > button')
            button.click()
            print("Login Successful")
        else:
            # User has no 2F
            print("Login Successful, no 2F")
        # Go to User's Instagram Page
        time.sleep(2)
