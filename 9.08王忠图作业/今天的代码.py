#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
import os
# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/')
# a=dr.find_element_by_css_selector('a.red')
# print(a.get_attribute('href'))
# dr.quit()
#
# da=webdriver.Firefox()
# da.get('http://39.96.181.61/qftest-ds/')
# b=da.find_element_by_xpath('//form[1]')
# print(b.get_attribute('method'))
# da.quit()

# dr=webdriver.Firefox()
# dr.get('file:///'+os.path.abspath('1.html'))
# a=dr.find_elements_by_id('10')
# for i in a:
#     print(i.get_attribute('href'))
# dr.quit()


# dr=webdriver.Firefox()
# dr.get('file:///'+os.path.abspath('1.html'))
# a=dr.find_elements_by_name('ccc')
# for i in a:
#     print(i.get_attribute('id'))
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('file:///'+os.path.abspath('1.html'))
# a=dr.find_elements_by_link_text('我是链接')
# for i in a:
#     print(i.get_attribute('id'))
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('file:///'+os.path.abspath('1.html'))
# a=dr.find_elements_by_link_text('aa')
# for i in a:
#     print(i.get_attribute('name'))
# dr.quit()
#

# dr=webdriver.Firefox()
# dr.get('file:///'+os.path.abspath('1.html'))
# a=dr.find_elements_by_tag_name('p')
# for i in a:
#     print(i.get_attribute('id'))
# dr.quit()
#

# dr=webdriver.Firefox()
# dr.get('file:///'+os.path.abspath('1.html'))
# a=dr.find_elements_by_class_name('myclass')
# print(a[0].get_attribute('id'))
# print(a[1].get_attribute('id'))
# dr.quit()

# dr=webdriver.Firefox()
# dr.get('file:///'+os.path.abspath('1.html'))
# a=dr.find_elements_by_xpath('//form[*]')
# for i in a:
#     print(i.get_attribute('id'))
# dr.quit()

dr=webdriver.Firefox()
dr.get('file:///'+os.path.abspath('1.html'))
a=dr.find_elements_by_css_selector('p.myclass')
for i in a:
    print(i.get_attribute('id'))
dr.quit()


