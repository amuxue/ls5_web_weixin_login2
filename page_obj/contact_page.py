from page_obj.basepage import BasePage

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_obj.add_depart_page import AddDepartPage
class ContactPage(BasePage):
    clickNode=(By.CSS_SELECTOR, ".member_colLeft_top_addBtnWrap.js_create_dropdown")
    addPart=(By.CSS_SELECTOR, ".js_create_party")
    partListNode=(By.CSS_SELECTOR, ".js_editable .jstree-anchor")

    def goto_add_depart_page(self):
        self.findElement(*self.clickNode).click()
        self.findElement(*self.addPart).click()

        return AddDepartPage(self.driver)

    def get_deport_list(self):
        self.driver:WebDriver
        sleep(5)
        deport_els=self.findElements(*self.partListNode)
        deport_list=[]
        for deport in deport_els:
            deport_list.append(deport.text)
        return deport_list
