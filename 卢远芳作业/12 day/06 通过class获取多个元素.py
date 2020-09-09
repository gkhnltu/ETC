#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get('http://www.taobao.com')
# e=dr.find_elements_by_class_name('site-nav-arrow')
# print(len(e))
#
# for i in e:
#     if i.get_attribute('id'):
#         print(i.get_attribute('id'))
#
# dr.quit()

#案例:自己写一个有类样式的html页面,定义段落和链接标签,引用类样式,然后通过本函数获取这两个标签的其他属性
from selenium import webdriver
import os
dr=webdriver.Firefox()
dr.get("file:///"+os.path.abspath("class-案列.html"))
e=dr.find_elements_by_class_name("mylist")
# print(len(e))
for i in e:
    print(i.get_attribute("href"))
dr.quit()