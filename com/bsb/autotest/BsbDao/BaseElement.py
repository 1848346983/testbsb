# _*_ coding:utf-8 _*_
from BsbDao.BasicInit import BasicInit
from appium.webdriver.mobilecommand import MobileCommand
import time
class BaseElement:
    def __init__(self):
        bas = BasicInit()
        self.driver =bas.get_driver()


    def get_id(self, id):
        element = self.driver.find_element_by_id(id)
        return element

    def get_xpath(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        print element
        return element

    def get_name(self, name):
        element = self.driver.find_element_by_name(name)
        return element

    def get_screen(self, path):
        self.driver.get_screenshot_as_file(path)

    def get_size(self):
        size = self.driver.get_window_size()
        return size

    def swipe_to_up(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

    def swipe_to_down(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)

    def swipe_to_left(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)

    def swipe_to_right(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

    def back(self):
        self.driver.keyevent(4)

    def get_classes(self, classesname):
        elements = self.driver.find_elements_by_class_name(classesname)
        return elements

    def get_ids(self, ids):
        elements = self.driver.find_elements_by_id(ids)
        return elements

    def switch_h5(self,context_name):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": context_name})


    def switch_app(self,NATIVE_APP):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": NATIVE_APP})

    def get_web_view(self):
        time.sleep(30)
        print('开始切换')
        # 获取当前界面的所有窗口
        WebView = self.driver.contexts
        print(WebView)
        View = WebView[1]
        print(View)
        # 切换到Webview窗口
        self.driver.switch_to.context(View)
        # 获取当前所处的环境窗口
        New_View = self.driver.current_context
        print('New_View is :', New_View)
        # 切换到NATIVE窗口
        self.driver.switch_to.context(WebView[0])
        # 获取当前所处的环境窗口
        New_View = self.driver.current_context
        print('New_View is :', New_View)