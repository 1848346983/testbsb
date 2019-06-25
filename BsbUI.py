# _*_ coding:utf-8 _*_
from appium import webdriver
import logging
import traceback
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

class initlogin :

    def login(self):
        logging.basicConfig(filename='Logs/'+'bsb.log',format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]',level=logging.INFO,filemode='a' ,datefmt='%a, %d %b %Y %H:%M:%S')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.1.0'
        desired_caps['deviceName'] = 'V1818A'
        desired_caps['appPackage'] = 'com.fotron.bsb'
        desired_caps['appActivity'] = '.ui.activity.MainActivity'

        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        logging.info('=======================================================================')
        time.sleep(6)
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.View[4]").click()

        logging.info('点击我的按钮，正常跳转到我的界面')
        driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[contains(@text,'登录')]").click()
        logging.info('在我的登录界面，点击登录按钮正常跳转到微信登录界面')
        driver.find_element_by_id('com.fotron.bsb:id/btn_wx_login').click()
        logging.info('点击微信登录，用户正常登录成功')
        print (driver.find_element_by_id('com.fotron.bsb:id/tv_me_id').text)
        userout = driver.find_element_by_id('com.fotron.bsb:id/tv_me_id').text

        if(str(userout) =='ID:61160909' ):

            logging.info('校验用户id：'+userout+',用户id正确')
        else :
            logging.info('用户id不正确,你的id为：'+userout)


        driver.find_element_by_xpath('//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.View[1]').click()
        logging.info('点击首页按钮，正常跳转首页界面')
        size = driver.get_window_size()
        x =size['width']
        y =size['height']
        print x
        print y
        driver.swipe(x * 0.5, 1000, x * 0.5,700, 1000)#向上
        time.sleep(1)
        driver.swipe(x * 0.5, 1000, x * 0.5, 300, 1000)  # 向上
        #zhuanqu = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[2]/android.widget.ScrollView/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]').text
        #zhuanqu = driver.find_element_by_xpath("//android.widget.TextView[@instance='14']").text
        zhuanqu = driver.find_elements_by_id('com.fotron.bsb:id/tv_special_area_name')[0].text
        time.sleep(1)
        print str(zhuanqu)
        if(str(zhuanqu)=='闪兑专区'):
            logging.info('向上滑动正常，闪兑专区显示出来')
            driver.swipe(x * 0.5, 1400, x * 0.5, 100, 1000)  # 向上
            time.sleep(1)

            driver.swipe(x * 0.5, 1400, x * 0.5, 100, 1000)  # 向上滑到底
            time.sleep(1)
            driver.swipe(x * 0.5, 300, x * 0.5, 1000, 1000)  # 向下滑动一段位置
            time.sleep(1)

        else :
            logging.info('向上滑动不正常，闪兑专区没有显示出来')
        remen = driver.find_element_by_xpath('//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[2]/android.widget.ScrollView/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]').text
        print remen
        if(str(remen)=='邀请专区'):
            logging.info('向下滑动正常')
        else:
            logging.info('滑动不成功还在底部')

        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[2]/android.widget.ScrollView/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[contains(@text,'更多')]").click()
        logging.info('进入更多页面')
        driver.find_element_by_xpath("//android.widget.TextView[@text='闪兑专区']").click()
        logging.info('在更多里面点击闪兑专区')
        driver.find_elements_by_id('com.fotron.bsb:id/iv_goods_img')[3].click()
        driver.swipe(360, 1400, 360, 100, 300)  # 向上

if __name__ == '__main__':
    try:
        logining = initlogin()
        logining.login()
    except:
        logging.exception(traceback.print_exc())




