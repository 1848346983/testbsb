#! -*-cording:utf-8 -*-
import unittest
from appium import webdriver
import time
from  com.bsb.autotest.BsbDao.ElementConfig import *
from  com.bsb.autotest.BsbDao.BasicInit import *


class MyTestCase(unittest.TestCase):





    def test_01_MY(self):
        element = ElementConfig()
        time.sleep(8)
        element.myclick()



    def tearDown(self):
        base = BasicInit()
        time.sleep(3)
        base.quit()






if __name__ == '__main__':
    unittest.main()





