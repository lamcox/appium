#coding:utf-8
from appium import webdriver
import time
import unittest
import sys
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
from common import login
from common import common

class HomeTest(unittest.TestCase):
    """首页"""

    @classmethod
    def setUpClass(cls):
        desired_caps = common.get_desiredCaps()
        url = common.url()
        global driver
        driver = webdriver.Remote(url, desired_caps)
        print("running test：首页")
        login.login(driver)
        time.sleep(2)

    def test_home_a(self):
        """未连接状态点击今日步数"""
        driver.find_element_by_id("com.happy.food:id/refreshStep").click()
        time.sleep(0.3)
        driver.get_screenshot_as_file("./result/screen/"+common.deviceModel()+'_'+sys._getframe().f_code.co_name+'.png')
        title = driver.find_element_by_id("com.happy.food:id/title").text
        self.assertEqual(title, "开心粮票")

    def test_home_b(self):
        """下拉刷新"""
        driver.swipe(start_x=540,start_y=410,end_x=540,end_y=1000,duration=500)
        time.sleep(3)
        try:
            button = driver.find_element_by_xpath("//android.widget.Button[contains(@text,'允许')]")
            button.click()
        except:
            pass
        driver.get_screenshot_as_file("./result/screen/"+common.deviceModel()+'_'+sys._getframe().f_code.co_name+'.png')
        title = driver.find_element_by_id("com.happy.food:id/title").text
        self.assertEqual(title,"开心粮票")

    def test_home_c(self):
        """进入我的页面"""
        driver.find_element_by_id("com.happy.food:id/mine").click()
        time.sleep(1)
        driver.get_screenshot_as_file("./result/screen/"+common.deviceModel()+'_'+sys._getframe().f_code.co_name+'.png')
        TextView = driver.find_elements_by_class_name("android.widget.TextView")
        text = TextView[0].text
        self.assertEqual("我的",text)

    def test_home_d(self):
        """我的页面返回"""
        driver.find_element_by_id("com.happy.food:id/back").click()
        time.sleep(1)
        driver.get_screenshot_as_file("./result/screen/"+common.deviceModel()+'_'+sys._getframe().f_code.co_name+'.png')
        title = driver.find_element_by_id("com.happy.food:id/title").text
        self.assertEqual(title,"开心粮票")

    def test_home_e(self):
        """进入通知页面"""
        driver.find_element_by_id("com.happy.food:id/message").click()
        time.sleep(1)
        driver.get_screenshot_as_file("./result/screen/"+common.deviceModel()+'_'+sys._getframe().f_code.co_name+'.png')
        TextView = driver.find_elements_by_class_name("android.widget.TextView")
        text = TextView[0].text
        self.assertEqual("消息",text)

    def test_home_f(self):
        """消息页面返回"""
        driver.find_element_by_id("com.happy.food:id/back").click()
        time.sleep(1)
        driver.get_screenshot_as_file("./result/screen/"+common.deviceModel()+'_'+sys._getframe().f_code.co_name+'.png')
        title = driver.find_element_by_id("com.happy.food:id/title").text
        self.assertEqual(title,"开心粮票")

    def test_home_g(self):
        """进入钱包页面"""
        driver.find_element_by_id("com.happy.food:id/myWallet").click()
        time.sleep(1)
        driver.get_screenshot_as_file("./result/screen/"+common.deviceModel()+'_'+sys._getframe().f_code.co_name+'.png')
        TextView = driver.find_elements_by_class_name("android.widget.TextView")
        text = TextView[0].text
        self.assertEqual("能量中心",text)

    def test_home_h(self):
        """钱包页面返回"""
        driver.find_element_by_id("com.happy.food:id/back").click()
        time.sleep(1)
        driver.get_screenshot_as_file("./result/screen/"+common.deviceModel()+'_'+sys._getframe().f_code.co_name+'.png')
        title = driver.find_element_by_id("com.happy.food:id/title").text
        self.assertEqual(title,"开心粮票")


    def test_home_i(self):
        """进入我的设备页面"""
        driver.find_element_by_id("com.happy.food:id/deviceStatus").click()
        time.sleep(1)
        driver.get_screenshot_as_file("./result/screen/"+common.deviceModel()+'_'+sys._getframe().f_code.co_name+'.png')
        TextView = driver.find_elements_by_class_name("android.widget.TextView")
        text = TextView[0].text
        self.assertEqual("我的设备",text)

    def test_home_j(self):
        """我的设备页面返回"""
        driver.find_element_by_id("com.happy.food:id/back").click()
        time.sleep(1)
        driver.get_screenshot_as_file("./result/screen/"+common.deviceModel()+'_'+sys._getframe().f_code.co_name+'.png')
        title = driver.find_element_by_id("com.happy.food:id/title").text
        self.assertEqual(title,"开心粮票")

    def test_home_k(self):
        """搜索设备"""
        driver.find_element_by_id("com.happy.food:id/deviceStatus").click()
        driver.wait_activity(".activity.MyDeviceActivity",1)
        driver.find_element_by_id("com.happy.food:id/deviceAction").click()
        time.sleep(1)
        try:  #自动点击app授权弹框
            button = driver.find_element_by_xpath("//android.widget.Button[contains(@text,'允许')]")
            button.click()
        except:
            pass
        time.sleep(1)
        try:
            button = driver.find_element_by_xpath("//android.widget.Button[contains(@text,'允许')]")
            button.click()
        except:
            pass
        time.sleep(2)
        driver.get_screenshot_as_file("./result/screen/"+common.deviceModel()+'_'+sys._getframe().f_code.co_name+'.png')
        TextView = driver.find_elements_by_class_name("android.widget.TextView")
        text = TextView[0].text
        self.assertEqual("搜索设备",text)

    def test_home_l(self):
        """点击搜索搜索"""
        driver.find_element_by_id("com.happy.food:id/searchDevice").click()
        time.sleep(0.5)
        driver.get_screenshot_as_file("./result/screen/"+common.deviceModel()+'_'+sys._getframe().f_code.co_name+'.png')
        TextView = driver.find_elements_by_class_name("android.widget.TextView")
        text = TextView[0].text
        self.assertEqual("搜索设备",text)

    def test_home_m(self):
        """搜索设备返回"""
        driver.find_element_by_id("com.happy.food:id/back").click()
        time.sleep(1)
        driver.get_screenshot_as_file("./result/screen/"+common.deviceModel()+'_'+sys._getframe().f_code.co_name+'.png')
        TextView = driver.find_elements_by_class_name("android.widget.TextView")
        text = TextView[0].text
        self.assertEqual("我的设备",text)

    @classmethod
    def tearDownClass(cls):
        driver.quit()

if __name__ == '__main__':
    unittest.main()