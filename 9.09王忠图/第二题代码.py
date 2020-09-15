#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
from time import sleep

def Acc(ac):
   with open(ac,'r',encoding='utf8') as f:
      a=f.read().splitlines()
   a1=(a[1])#网址
   a2=(a[3])#帐号
   a3=(a[5])#密码

   dr=webdriver.Firefox()
   dr.get(a1)
   a=dr.find_element_by_id('username')
   a.send_keys(a2)
   b=dr.find_element_by_id('password')
   b.send_keys(a3)
   c=dr.find_element_by_link_text('登 陆')
   c.click()
   sleep(10)
   dr.get_screenshot_as_file('01.png')
   dr.quit()

Acc('01.txt')
