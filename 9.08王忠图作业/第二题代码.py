#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
dr=webdriver.Firefox()
dr.get('http://39.96.181.61/qftest-ds/')
a=dr.find_element_by_css_selector('a.red')
print(a.get_attribute('href'))
dr.quit()

da=webdriver.Firefox()
da.get('http://39.96.181.61/qftest-ds/')
b=da.find_element_by_xpath('//form[1]')
print(b.get_attribute('method'))
da.quit()

