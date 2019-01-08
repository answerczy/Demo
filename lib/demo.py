# -*- coding = utf-8 -*-
"""
python version:3.5.2
selenium version:3.3.1
Firefox version:49
"""
from selenium import webdriver
import time
import unittest
class Demo(unittest.TestCase):
    def Testmethod(self):
        driver = webdriver.Chrome()
        driver.get("http://www.amazon.cn")
        driver.maximize_window()
        time.sleep(5)
        driver.find_element_by_xpath(".//*[@id='twotabsearchtextbox']").send_keys("软件测试")
        driver.find_element_by_xpath(".//*[@id='nav-search']/form/div[2]/div/input").click()
        #choice book name is software testing
        time.sleep(5)
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_xpath('//*[@id="result_0"]/div/div[3]/div[1]/a/h2').click()
        #add book into cart
        time.sleep(5)
        driver.switch_to_window(driver.window_handles[1])
        driver.find_element_by_xpath(".//*[@id='add-to-cart-button']").click()
        #Assert
        time.sleep(10)
        driver.switch_to_window(driver.window_handles[1])
        try:
            self.assertEquals('商品已加入购物车',driver.find_element_by_xpath(".//*[@id='huc-v2-order-row-messages']").text)
            print('商品已经加入购物车！！')
        except:
            print('商品未加入购物车！')
        try:
            self.assertEquals('￥ 20.40',driver.find_element_by_xpath(".//*[@id='hlb-subcart']/div[1]/span/span[2]").text)
            print('商品的价格为：',driver.find_element_by_xpath(".//*[@id='hlb-subcart']/div[1]/span/span[2]").text)
        except:
            print('商品的价格不为20.40！')
            print('商品的价格为：',driver.find_element_by_xpath(".//*[@id='hlb-subcart']/div[1]/span/span[2]").text)


d1 = Demo()
d1.Testmethod()

# if __name__ == '__main__':
#     unittest.main()



