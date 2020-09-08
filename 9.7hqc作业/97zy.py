#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#3.请在电商网站上找10个元素,用id和name方式获取,打印元素
# 除id和name外的其他属性, 提交到git上
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_element_by_name('kw')
# print(e.get_attribute('class'))
# dr.quit()

# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_element_by_name('qty')
# print(e.get_attribute('type'))
# dr.quit()

# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_element_by_name('keywords')
# print(e.get_attribute('content'))
# dr.quit()

# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_element_by_name('verydows-baseurl')
# print(e.get_attribute('content'))
# dr.quit()

# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_element_by_name('description')
# print(e.get_attribute('content'))
# dr.quit()

#id1:
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_element_by_id('logined-userbar-tpl')
# print(e.get_attribute('type'))
# dr.quit()

# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_element_by_id('buy-form')
# print(e.get_attribute('action'))
# dr.quit()

# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_element_by_id('buy-qty')
# print(e.get_attribute('class'))
# dr.quit()

# from selenium import webdriver
# # dr=webdriver.Firefox()
# # dr.get("http://39.96.181.61/qftest-ds/")
# # e=dr.find_element_by_id('review-tpl')
# # print(e.get_attribute('type'))
# # dr.quit()

# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_element_by_id('vdspoploginbar')
# print(e.get_attribute('class'))
# dr.quit()
#4.电商网站上找5个超链接元素,通过超链接文字获取元素,打印链接地址,提交到git上
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/goods/index.html?id=255')
# e=dr.find_element_by_link_text('网站首页')
# print(e.get_attribute('href'))
# dr.quit()

# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/goods/index.html?id=255')
# e=dr.find_element_by_link_text('首页')
# print(e.get_attribute('href'))
# dr.quit()

# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/goods/index.html?id=255')
# e=dr.find_element_by_link_text('dsfs')
# print(e.get_attribute('href'))
# dr.quit()

# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get('http://39.96.181.61/qftest-ds/goods/index.html?id=255')
# e=dr.find_element_by_link_text('中国')
# print(e.get_attribute('href'))
# dr.quit()

from selenium import webdriver
dr=webdriver.Firefox()
dr.get('http://39.96.181.61/qftest-ds/goods/index.html?id=255')
e=dr.find_element_by_link_text('dady')
print(e.get_attribute('href'))
dr.quit()