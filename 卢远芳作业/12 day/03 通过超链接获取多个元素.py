#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/')
# e=dr.find_elements_by_link_text('[美食专栏]诗词')
# print(len(e))
# for i in e:
#     print(i.get_attribute('href'))
#
# dr.quit()

#案列：电商网站：
from selenium import webdriver
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/")
e=dr.find_elements_by_link_text("烧猪")
print(len(e))
for i in e:
    print(i.get_attribute("href"))

dr.quit()