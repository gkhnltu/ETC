#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
from time import sleep
def Ass(a):
    dr=webdriver.Firefox()
    dr.get('https://www.xiaomiyoupin.com')
    sleep(5)
    for i in range(0,10000,a):
        dr.execute_script("document.documentElement.scrollTop=%d"%i)
        sleep(1)

Ass(50)






