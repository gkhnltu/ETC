#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# from selenium import webdriver
#
# dr=webdriver.Firefox()
# dr.get("https://www.baidu.com")
# e=dr.find_elements_by_tag_name('div')
# print(len(e))
#
# dr.quit()

#案例:获取淘宝首页有多少个div,并打印出div里的id属性值
from selenium import webdriver
dr=webdriver.Firefox()
dr.get("https://www.taobao.com")
e=dr.find_elements_by_tag_name('div')
print(len(e))
dr.quit()

