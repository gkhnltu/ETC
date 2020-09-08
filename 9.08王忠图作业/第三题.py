#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
import os
#id获取元素：
# dr=webdriver.Firefox()
# dr.get('file:///'+os.path.abspath('1.html'))
# a=dr.find_elements_by_id('10')
# print(a[0].get_attribute('href'))
# print(a[1].get_attribute('href'))
# dr.quit()

#name获取元素：
# ab=webdriver.Firefox()
# ab.get('file:///'+os.path.abspath('1.html'))
# b=ab.find_elements_by_name('ccc')
# print(b[0].get_attribute('id'))
# print(b[1].get_attribute('href'))
# ab.quit

#链接文本定位：
# ac=webdriver.Firefox()
# ac.get('file:///'+os.path.abspath('1.html'))
# c=ac.find_elements_by_link_text('我是链接')
# print(c[0].get_attribute('id'))
# print(c[1].get_attribute('id'))
# ac.quit()

#子链接：
# ad=webdriver.Firefox()
# ad.get('file:///'+os.path.abspath('1.html'))
# d=ad.find_element_by_partial_link_text('aa')
# print(d.get_attribute('href'))
# print(d.get_attribute('name'))
# ad.quit()

# 标签名
# ae=webdriver.Firefox()
# ae.get('file:///'+os.path.abspath('1.html'))
# e=ae.find_elements_by_tag_name('p')
# print(e[0].get_attribute('id'))
# print(e[1].get_attribute('id'))
# ae.quit()

# class
# af=webdriver.Firefox()
# af.get('file:///'+os.path.abspath('1.html'))
# f=af.find_elements_by_class_name('myclass')
# print(f[0].get_attribute('id'))
# print(f[1].get_attribute('id'))
# af.quit()

# 路径
# ag=webdriver.Firefox()
# ag.get('file:///'+os.path.abspath('1.html'))
# g=ag.find_elements_by_xpath('//form[*]')
# print(g[0].get_attribute('id'))
# print(g[1].get_attribute('id'))
# ag.quit()

# css
ah=webdriver.Firefox()
ah.get('file:///'+os.path.abspath('1.html'))
h=ah.find_elements_by_css_selector('p.myclass')
for i in h:
    print(i.get_attribute('id'))
ah.quit()