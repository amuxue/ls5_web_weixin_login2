import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    driver: webdriver

    def __init__(self,driver=None):

        if(driver==None):
            self.driver = webdriver.Chrome()
            self.cookie_login()
        else:
            self.driver=driver
        self.driver.implicitly_wait(3)


    def cookie_login(self):
        self.driver.get("https://work.weixin.qq.com")
        with open("cookies.json", "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    def findElement(self,By,patterm):
        return self.driver.find_element(By, patterm)

    def findElements(self,By,patterm):
        return self.driver.find_elements(By, patterm)