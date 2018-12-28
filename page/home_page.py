import allure

from base.base_action import BaseAction
import page

"""
负责首页页面逻辑
"""
class HomePage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    #点击我的
    @allure.step('点击首页 我')
    def click_my(self):
        self.click_element(page.home_page_me_btn)