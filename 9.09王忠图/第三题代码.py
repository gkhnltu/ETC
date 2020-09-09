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
   a1=(a[7])#网址

   dr=webdriver.Firefox()
   dr.get(a1)
   aa=dr.find_element_by_name('kw')
   aa.send_keys('苹果')
   b=dr.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/form/div/button')
   b.click()
   sleep(6)
   c=dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[2]/div[2]/ul/li[1]/div/a/img')
   c.click()
   d=dr.find_element_by_link_text('加入购物车')
   d.click()
   sleep(6)
   dr.quit()


Acc('01.txt')