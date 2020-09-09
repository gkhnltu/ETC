#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# 三．自动化登入电商系统前台，把苹果加入到购物车
# 注意：网站要通过代码获取
from selenium import webdriver
from time import sleep
f=open("dll.txt",'r')
qt=f.readline()
print(qt)

dr=webdriver.Firefox()
dr.get(qt)
sleep(5)
e=dr.find_element_by_name("kw")
sleep(2)
e.send_keys('苹果')
e.submit()

dr.find_element_by_link_text("苹果").click()
sleep(8)
dr.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/div[4]/a[1]").clink()
sleep(2)
dr.quit()



