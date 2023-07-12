import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "C:\ChromeDriver-for-Selenium\chromedriver.exe"
SIMILAR_ACCOUNT = "buzzfeedtasty"
USERNAME = os.environ['INSTA_ACC']
PASSWORD = os.environ['INSTA_PASS']


class InstaFollower:

    def __init__(self, path):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.service = Service(executable_path=path)
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        time.sleep(4)
        modal = self.driver.find_element(By.CSS_SELECTOR, 'div._aano')

        # Scroll down in modal window
        for i in range(3):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(1)

        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'div._aano  button._acan._acap._acas._aj1-')

        # print the number of buttons found
        print(f"Found {len(buttons)} buttons")
        time.sleep(1)

        return buttons

    def follow(self, buttons):
        for button in buttons:
            try:
                # button.click()

                # Simulate following...
                print(button.text)
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
followers_buttons = bot.find_followers()
bot.follow(followers_buttons)
