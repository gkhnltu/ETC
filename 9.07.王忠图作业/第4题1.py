#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# 4.电商网站上找5个超链接元素,通过超链接文字获取元素,打印链接地址,提交到git上
from selenium import webdriver
dr=webdriver.Firefox()
dr.get('http://39.96.181.61/qftest-ds/')
a=dr.find_element_by_link_text("首页")
print(a.get_attribute('href'))
dr.quit()
