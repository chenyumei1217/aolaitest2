"""
1、设置包名和启动名

"""
from selenium.webdriver.common.by import By

appPackage = 'com.yunmall.lc'
appActivity = 'com.yunmall.ymctoc.ui.activity.MainActivity'
"""
2、首页

"""
home_page_me_btn = (By.ID,"com.yunmall.lc:id/tab_me")


"""
3、注册页面
"""
sing_in_page_exist_count=(By.ID,"com.yunmall.lc:id/gotologon")

"""
4、登录页面
"""
login_page_username=(By.ID,"com.yunmall.lc:id/logon_account_textview")
login_page_password=(By.ID,"com.yunmall.lc:id/logon_password_textview")
login_page_btn=(By.ID,"com.yunmall.lc:id/logon_button")
login_page_close_btn=(By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image")

"""
5、个人中心页面
"""
person_center_setting=(By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image")
person_center_order_all=(By.ID,"com.yunmall.lc:id/order_more_txt")

"""
6、设置页面
"""
setting_exit=(By.ID,"com.yunmall.lc:id/setting_logout")
setting_exit_enter=(By.ID,"com.yunmall.lc:id/ymdialog_right_button")




