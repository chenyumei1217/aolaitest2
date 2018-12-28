import allure

from base.base_action import BaseAction
import page

"""
负责个人中心页面逻辑
"""
class PersonCenterPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)
    #点击个人中心 设置
    @allure.step('进入个人中心设置页面')
    def click_setting_btn(self):
        self.click_element(page.person_center_setting)
    #判断一下是否登录成功，登录成功返回true 登录失败返回false
    @allure.step('判断登录是否成功')
    def is_login_sucess(self):
        try:
            self.find_element(page.person_center_order_all)
            return True
        except:
            return False
