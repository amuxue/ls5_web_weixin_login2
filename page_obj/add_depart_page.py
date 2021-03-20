from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from page_obj.basepage import BasePage


class AddDepartPage(BasePage):
    partName=(By.CSS_SELECTOR, "input[name=name]")
    partChoose=(By.CSS_SELECTOR, "#__dialog__MNDialog__ .inputDlg_item .js_toggle_party_list")
    partNode=(By.CSS_SELECTOR, ".qui_dropdownMenu.ww_dropdownMenu [id='1688853554820852_anchor']")
    submit_bt=(By.CSS_SELECTOR,"[d_ck=submit]")


    def addDepart(self,name):
        self.findElement(*self.partName).send_keys(name)
        # 点击选择部门
        self.findElement(*self.partChoose).click()
        sleep(5)
        # 选择部门
        self.findElement(*self.partNode).click()
        sleep(3)
        self.findElement(*self.submit_bt).click()
        from page_obj.contact_page import ContactPage
        return ContactPage(self.driver)