
from page_obj.main_page import MainPage

class TestAddDepart():

    def test_add_depart_case(self):
       partName="第一个部门"
       result=MainPage().goto_contact_page().goto_add_depart_page().addDepart(partName).get_deport_list()

       assert (partName in result,"添加部门失败")

