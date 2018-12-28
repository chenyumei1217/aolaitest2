import allure

from base.base_action import BaseAction
import page

#负责登录页面逻辑
class LoginPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    @allure.step('登录逻辑')
    def click_login(self,username,password):
        allure.attach('登录步骤', '输入用户名')
        self.input_element(page.login_page_username,username)
        allure.attach('登录步骤', '输入密码')
        self.input_element(page.login_page_password,password)
        allure.attach('登录步骤', '点击登录按钮')
        self.click_element(page.login_page_btn)

    @allure.step('关闭登录页面')
    def click_close_btn(self):
        self.click_element(page.login_page_close_btn)
