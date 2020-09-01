import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Mobile Login
class mobileLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sign_in(self):

        """
        Function that signs in automatically into Instagram with a specified username and password.
        Note: This function takes into consideration TwoFact Authentication.
        Variables:
        Self: self
        expected_url: URL of Instagram 2F if enabled.
        :return: None, opens an instance of Chrome and automatically logs in.
        """
        mobile_emulation = {

            "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},

            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

        options = Options()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome(options=options, executable_path="C://Users/Brianna's HP17/Desktop/chromedriver.exe")
        driver.get(url="http://instagram.com")

        print('Signing In...')
        # Clicks on Login Button
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
            '#react-root > section > main > article > div > div > div > div:nth-child(2) > button')))
        button.click()

        # Looks for username in a specific amount of time, enough for webpage to load
        user_id = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,
            '#loginForm > div.Igw0E.IwRSH.eGOV_._4EzTm.kEKum > div:nth-child(3) > div > label > input')))
        user_id.click()
        user_id.send_keys(self.username)

        # Looks for password in a specific amount of time, enough for webpage to load
        pwd = driver.find_element_by_css_selector(
            '#loginForm > div.Igw0E.IwRSH.eGOV_._4EzTm.kEKum > div:nth-child(4) > div > label > input')
        pwd.click()
        pwd.send_keys(self.password)

        # Second login button
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
            '#loginForm > div.Igw0E.IwRSH.eGOV_._4EzTm.kEKum > div:nth-child(6) > button')))
        button.click()

        # Add to Homescreen Button -> Cancel
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
            'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')))
        button.click()

        # Click on Profile
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
            '# react-root > section > main > section > div:nth-child(2) > div:nth-child(1) > div > '
            'article:nth-child(1) > header > div.o-MQd > div:nth-child(1) > div > a')))
        button.click()


        time.sleep(7)
