#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# 二．自动化登入电商系统后台,登入后截图
# 注意：网站,用户名和密码要通过代码获取
from selenium import webdriver
from time import sleep
f=open("dll.txt","r")
all=f.read().splitlines()
ht=(all[1])
yh=[all[2]]
mm=(all[3])
print(mm)
print(ht)
dr=webdriver.Firefox()
dr.get(ht)
sleep(2)
e=dr.find_element_by_id("username")
e.send_keys(yh)
sleep(2)
e1=dr.find_element_by_id("password")
sleep(2)
e1.send_keys(mm)
sleep(2)
e3=dr.find_element_by_class_name("btn.unslt")
e3.click()









