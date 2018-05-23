#coding=utf-8
import unittest
from time import sleep
from appium import webdriver
import sys
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
from common import common

class Login(unittest.TestCase):
    """登录测试"""

    @classmethod
    def setUpClass(cls):
        desired_caps = common.get_desiredCaps()
        url = common.url()
        global driver
        driver = webdriver.Remote(url,desired_caps)
        print("running test：登录")
        sleep(3)

    def test_login_a(self):
        """密码大写小验证"""
        EditText = driver.find_elements_by_class_name("android.widget.EditText")
        EditText[0].send_keys("13410066133")
        EditText[1].send_keys("1234567A")
        driver.find_element_by_id("com.happy.food:id/login").click()
        sleep(1)
        driver.get_screenshot_as_file(
            "./result/screen/" + common.deviceModel() + '_' + sys._getframe().f_code.co_name + '.png')
        Text = driver.find_element_by_id("com.happy.food:id/login").text
        self.assertEqual(Text,"登陆")

    def test_login_b(self):
        """登录成功"""
        EditText = driver.find_elements_by_class_name("android.widget.EditText")
        EditText[0].clear()
        EditText[0].send_keys("13410066133")
        EditText[1].clear()
        EditText[1].send_keys("1234567a")
        driver.find_element_by_id("com.happy.food:id/login").click()
        sleep(2)
        try:
            driver.find_element_by_xpath("//android.widget.Button[contains(@text,'允许')]").click()
        except:
            pass
        sleep(1)
        driver.get_screenshot_as_file("./result/screen/" + common.deviceModel() + '_' + sys._getframe().f_code.co_name + '.png')
        title = driver.find_element_by_id("com.happy.food:id/title").text
        self.assertEqual(title,'开心粮票')

    @classmethod
    def tearDownClass(cls):
        driver.quit()

if __name__ == '__main__':
    unittest.main()