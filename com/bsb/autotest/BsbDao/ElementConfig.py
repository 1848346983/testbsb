# _*_ coding:utf-8 _*_
from BaseElement import BaseElement
import logging
from appium import webdriver




class ElementConfig:

    # 点击我的按钮，进入我的页面
    def myclick(self):
        self.ele = BaseElement()
        #self.ele.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.View[4]").click()
        return self.ele.get_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.View[4]")
        logging.info("点击我的按钮，进入我的页面")
