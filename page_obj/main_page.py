from time import sleep


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_obj.basepage import BasePage



class MainPage(BasePage):
    contact_herf=(By.ID, "menu_contacts")

    def goto_contact_page(self):
        self.findElement(*self.contact_herf).click()
        from page_obj.contact_page import ContactPage
        return ContactPage(self.driver)