#_*_coding:utf8_*_
import time
import sys
from Selenium2Library import Selenium2Library

class MyGlh(object):
    def __init__(self):
        sys.setrecursionlimit(4000)

    def generate_client_num(self):
        """生成客户号"""
        num = 'test'+time.strftime('%Y%m%d%H%M%S',time.localtime())
        print "num==" + num
        return num
    def click_js(self,xpath):
        xpathElement = Selenium2Library.find_element(xpath)
        Selenium2Library._current_browser().execute_script('return argument[0].click()',xpathElement)

