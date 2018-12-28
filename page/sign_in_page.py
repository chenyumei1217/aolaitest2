import allure

from base.base_action import BaseAction
import page

"""
负责注册页面逻辑
"""
class SignInPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    @allure.step('点击 已有帐号去登录')
    def click_exits_account(self):
        self.click_element(page.sing_in_page_exist_count)


