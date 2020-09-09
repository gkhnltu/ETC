#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# 一．今天的代码敲一遍
# 二．自动化登入电商系统后台,登入后截图
# 注意：网站,用户名和密码要通过代码获取
with open("1.txt","r",encoding="gbk") as f:
    c = f.read().splitlines()
http=c[1]
user=c[3]
pas=c[5]

from  selenium import webdriver
from time import sleep
dr=webdriver.Firefox()
dr.get(http)
e=dr.find_element_by_id("username")
sleep(2)
e.send_keys(user)
sleep(2)
ee=dr.find_element_by_id('password')
sleep(2)
ee.send_keys(pas)
sleep(2)
dr.find_element_by_class_name("btn.unslt").click()
sleep(10)
dr.get_screenshot_as_file("9.9.png")
dr.quit()


# 三．自动化登入电商系统前台，输入框输入苹果，把苹果加入到购物车
# 注意：网站要通过代码获取
with open("1.txt","r",encoding="gbk")as f4:
    b=f4.read().splitlines()
http2=b[7]
# print(http2)

from selenium import webdriver
from time import sleep
dr=webdriver.Firefox()
dr.get(http2)
sleep(2)
dr.find_element_by_name("kw").send_keys("苹果")
sleep(2)
dr.find_element_by_tag_name("button").click()
sleep(2)
dr.find_element_by_link_text("苹果").click()
sleep(2)
dr.find_element_by_class_name("add-cart.icon").click()
sleep(2)
dr.quit()