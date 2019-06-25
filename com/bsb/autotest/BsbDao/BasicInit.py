# _*_ coding:utf-8 _*_
from appium import webdriver
import logging
import traceback
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

class BasicInit:
    """
    初始化
    """
    def __init__(self):
        #logging.basicConfig(filename='Logs/' + 'bsb.log', format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]',
        #                    level=logging.INFO, filemode='a', datefmt='%a, %d %b %Y %H:%M:%S')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.1.0'
        desired_caps['deviceName'] = 'V1818A'
        desired_caps['appPackage'] = 'com.fotron.bsb'
        desired_caps['appActivity'] = '.ui.activity.MainActivity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        time.sleep(5)



    def get_driver(self):
        return self.driver

    def quit(self):
        self.driver.quit()

