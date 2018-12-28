import sys , os ,time

import allure

sys.path.append(os.getcwd())
from base.read_yaml_data import read_yaml_data
from base.base_driver import init_driver
import page,pytest
from page.navigation_page import NavigationPage


#获取模拟的yaml数据
def getyaml():
    datalist = []
    yaml_data = read_yaml_data("login_data.yaml")
    for i in yaml_data:
        data = yaml_data.get(i)
        username = data.get("username")
        password = data.get("password")
        tag =data.get("tag")
        get_toast_msg = data.get("get_toast_msg")
        except_msg = data.get("except_msg")
        datalist.append((username, password,tag,get_toast_msg,except_msg))
    return datalist

class Test_Login():

    def setup_class(self):
        #初始化driver对象
        self.driver = init_driver(page.appPackage,page.appActivity)
        #初始化导航类
        self.navigation_page =NavigationPage(self.driver)

    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()

    #测试登录
    @allure.step('测试登录模块')
    @pytest.mark.parametrize("username,password,tag,,get_toast_msg,except_msg",getyaml())
    def test_login(self,username,password,tag,get_toast_msg,except_msg):
        #1、点击我的
        self.navigation_page.home_page_obj().click_my()
        #2、点击已有帐号去登录
        self.navigation_page.sign_in_page_obj().click_exits_account()
        #3、输入帐号密码注册
        self.navigation_page.login_page_obj().click_login(username,password)

        #判断tag，如果是1代表登录成功，0代表登录失败
        if tag == 1:
            try:
                is_success = self.navigation_page.person_center_obj().is_login_sucess()
                # 4、点击个人中心设置按钮
                self.navigation_page.person_center_obj().click_setting_btn()
                #5、点击退出
                self.navigation_page.setting_page_obj().logout_account()
                #断言，如果登录不成功，截图
                assert is_success,self.navigation_page.person_center_obj().get_screen()

            except:
                self.navigation_page.person_center_obj().get_screen()
                #关闭页面
                self.navigation_page.login_page_obj().click_close_btn()
        else:
            try:
                #获取吐司信息
                toast_message = self.navigation_page.person_center_obj().get_toast_message(get_toast_msg)
                assert toast_message == except_msg,self.navigation_page.person_center_obj().get_screen()
            finally:
                # 关闭页面
                self.navigation_page.login_page_obj().click_close_btn()

