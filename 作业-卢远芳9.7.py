#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# 1.简述自动化测试流程？

# 1.自动测试决定
# 2.测试工具获取
# 3.自动化测试引入
# 4.制定测试计划
# 5.测试执行与管理（脚本的运行、过程监控、结果管理）
# 6.测试审评和评估

# 2.简述自动化测试的优势和局限性？

# 优势：
# 1、可以解决日常重复，繁琐的测试工作，提高测试工作效率；
# 2、自动化测试可靠性高，测试精确度高；
# 3、提高测试资源的利用率
# 局限：
# 1、自动化测试是工具执行，没有思维，无法进行主观判断（列如色彩、布局、系统奔溃现象）；
# 2、对于需求更改频繁的软件，测试脚本的维护和设计比较困难；
# 3、自动化测试是机器执行，发现的问题比手工测试要少很多；
# 4、自动化测试工具本身是一个产品，在不同的系统平台或硬件平台可能会受影响，在运行时可能影响被测程序的测试结果。


# 3.请在电商网站上找10个元素,用id和name方式获取,打印元素除id和name外的其他属性,提交到git上

#####1、通过name获取元素：#####
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/index.html")
# e=dr.find_element_by_name("kw")
# print(e.get_attribute("placeholder"))
# dr.quit()

#####2、通过name获取元素：#####
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/goods/index.html?id=258")
# e1=dr.find_element_by_name("qty")
# print(e1.get_attribute("value"))
# dr.quit()

#####3、通过name获取元素：#####
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/goods/index.html?id=258")
# e1=dr.find_element_by_name("verydows-baseurl")
# print(e1.get_attribute("content"))
# dr.quit()

#####4、通过name获取元素：#####
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/goods/index.html?id=258")
# e=dr.find_element_by_name("description")
# print(e.get_attribute("content"))
# dr.quit()

#####5、通过name获取元素：#####
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/goods/index.html?id=258")
# e=dr.find_element_by_name("keywords")
# print(e.get_attribute("content"))
# dr.quit()

#####6、通过id获取元素：#####
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/goods/index.html?id=258")
# e=dr.find_element_by_id("top-userbar")
# print(e.get_attribute("class"))
# dr.quit()

#####7、通过id获取元素：#####
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/goods/index.html?id=258")
# e=dr.find_element_by_id("logined-userbar-tpl")
# print(e.get_attribute("type"))
# dr.quit()

#####8、通过id获取元素：#####
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/goods/index.html?id=258")
# e=dr.find_element_by_id("unlogined-userbar-tpl")
# print(e.get_attribute("type"))
# dr.quit()

#####9、通过id获取元素：#####
# from  selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/goods/index.html?id=258")
# e=dr.find_element_by_id("tmb-back-btn")
# print(e.get_attribute("class"))
# dr.quit()

#####10、通过id获取元素：#####
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/goods/index.html?id=258")
# e=dr.find_element_by_id("thumb-container")
# print(e.get_attribute("class"))
# dr.quit()


# 4.电商网站上找5个超链接元素,通过超链接文字获取元素,打印链接地址,提交到git上

#####1、通过超链接文字获取元素：#####
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_element_by_link_text("首页")
# print(e.get_attribute("href"))
# dr.quit()

#####2、通过超链接文字获取元素：#####
# from  selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_element_by_link_text("dsfs")
# print(e.get_attribute("href"))
# dr.quit()

#####3、通过超链接文字获取元素：#####
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_element_by_link_text("臭豆腐")
# print(e.get_attribute("href"))
# dr.quit()

#####4、通过超链接文字获取元素：#####
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_element_by_link_text("烧鹅")
# print(e.get_attribute("href"))
# dr.quit()

#####5、通过超链接文字获取元素：#####
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get("http://39.96.181.61/qftest-ds/")
# e=dr.find_element_by_link_text("小白")
# print(e.get_attribute("href"))
# dr.quit()