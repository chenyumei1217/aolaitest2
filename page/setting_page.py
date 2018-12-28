import allure

from base.base_action import BaseAction
import page

"""
    负责个人中心 设置 页面逻辑
"""
class SettingPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    @allure.step('退出当前登录帐号')
    def logout_account(self):
        #调用 滑动
        self.swipe_screen(1)
        #点击 退出按钮
        self.click_element(page.setting_exit)
        #点击确认退出
        self.click_element(page.setting_exit_enter)
