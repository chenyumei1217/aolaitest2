import time

import allure
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


class BaseAction:
    def __init__(self,driver):
        self.driver = driver

    def click_element(self,loc):
       self.find_element(loc).click()

    def input_element(self,loc,content):
        self.find_element(loc).send_keys(content)

    def long_click_element(self,loc):
        TouchAction(self.driver).long_press(self.find_element(loc)).release().perform()

    def find_element(self,loc):
        self.driver.implicitly_wait(10)
        return  self.driver.find_element(loc[0],loc[1])

    #实现滑动业务
    def swipe_screen(self,tag):
        time.sleep(1)
        screen_size=self.driver.get_window_size()
        width = screen_size.get("width")#获取手机宽度
        height = screen_size.get("height")#获取手机高度
        if tag == 1: #向上滚动
            self.driver.swipe(width * 0.5,height * 0.8,width * 0.5, height * 0.3,1000)
        if tag == 2: #向下滚动
            self.driver.swipe(width * 0.5,height * 0.3,width * 0.5, height * 0.8,1000)
        if tag == 3: #向左滚动
            self.driver.swipe(width * 0.8,height * 0.5,width * 0.3, height * 0.5,1000)
        if tag == 4: #向右滚动
            self.driver.swipe(width * 0.3,height * 0.5,width * 0.8, height * 0.5,1000)

    #获取吐司的消息
    @allure.step('获取吐司消息')
    def get_toast_message(self,message):
        toast_xpath="//*[contains(@text,'{}')]".format(message)
        toast_message =self.find_element((By.XPATH,toast_xpath)).text
        return toast_message

    #截屏
    @allure.step('截屏错误信息')
    def get_screen(self):
        png_name = "./screen/{}.png".format(int(time.time()))
        self.driver.get_screenshot_as_file(png_name)


