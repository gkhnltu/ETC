#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# 1、．在电商网上通过路径和css各找一个元素，并打印其他属性值，这里一个.py文件

#########1、通过路径查找元素##########

from selenium import webdriver
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/index.html")
e=dr.find_element_by_xpath("//input[@name='kw']")
print(e.get_attribute("placeholder"))
dr.quit()

#########2、通过路径查找元素##########

from selenium import webdriver
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/index.html")
# e=dr.find_element_by_xpath('//*form[1]')
e=dr.find_element_by_xpath("/html/body/div/div/div/div/form[1]")
print(e.get_attribute("method"))
dr.quit()

#########1、通过css查找元素##########

from selenium import webdriver
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/index.html")
e=dr.find_element_by_css_selector("div.topper-userbar")
print(e.get_attribute("id"))
dr.quit()

#########2、通过css查找元素##########

from selenium import webdriver
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/index.html")
e=dr.find_element_by_css_selector("a.red")
print(e.get_attribute("href"))
dr.quit()



# 2、．通过获取多个元素的方式获取元素，分别用id,name,链接文字，子链接文字，标签名，
# class,路径，css,在电商网上至少各自找2个以上元素，并打印出其他属性，这里一个.py文件

#########1、通过id查找多个元素##########
from selenium import webdriver
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/index.php?m=backend&c=main&a=panel")
e=dr.find_elements_by_id("pop-user")
# print(len(e))
for i in e:
    print(e._getattribute("class"))
dr.quit()


#########2、通过id查找多个元素##########
from selenium import webdriver
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/index.php?m=backend&c=main&a=panel")
e=dr.find_elements_by_id("header")
# print(len(e))
for i in e:
    print(e._getattribute("class"))
dr.quit()

#########1、通过name查找多个元素##########
from selenium import webdriver
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/index.php?m=backend&c=main&a=panel")
e=dr.find_elements_by_name("text/template")
# print(len(e))
for i in e:
    print(i.get_attribute("id"))

#########1、通过链接查找多个元素##########
from selenium import webdriver
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/")
e=dr.find_elements_by_link_text("臭豆腐")
print(len(e))
for i in e:
    print(i.get_attribute("href"))

dr.quit()

#########2、通过链接查找多个元素##########
from selenium import webdriver
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/")
e=dr.find_elements_by_link_text("小白")
print(len(e))
for i in e:
    print(i.get_attribute("href"))
dr.quit()

#########1、通过子链接查找多个元素##########
from selenium import webdriver
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/")
e=dr.find_elements_by_partial_link_text("[美食专栏]")
print(len(e))
for i in e:
    print(i.get_attribute("href"))
dr.quit()

#########2、通过子链接查找多个元素##########
from selenium import webdriver
import os
dr=webdriver.Firefox()
dr.get("file:///"+os.path.abspath("HTML-案例/partial_link-01.html"))
e=dr.find_elements_by_partial_link_text("aaa")
# print(e[0].get_attribute("href"))  #返回一个
for i in e:
    print(i.get_attribute("href")) #返回多个
dr.quit()

#########1、通过标签名查找多个元素##########
from selenium import webdriver
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/")
e=dr.find_elements_by_tag_name("div")
# print(len(e))
for i in e:
    if i.get_attribute("class"):
        print(i.get_attribute("class"))
dr.quit()

#########2、通过标签名查找多个元素##########
from selenium import webdriver
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/")
e=dr.find_elements_by_tag_name("a")
print(len(e))
for i in e:
    print(i.get_attribute("href"))
dr.quit()

#########1、通过class标签名查找多个元素##########
from selenium import webdriver
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/")
e=dr.find_elements_by_class_name("haschild")
print(len(e))
for i in e:
    print(i.get_attribute("href"))
dr.quit()


#########2、通过class查找多个元素##########
from selenium import webdriver
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/")
e=dr.find_elements_by_class_name("radius4.mt10")
print(len(e))
for i in e:
    print(i.get_attribute("href"))
dr.quit()


#########1、通过css标签名查找多个元素##########
from selenium import webdriver
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/")
e=dr.find_elements_by_css_selector("div.topper-links.fr")
print(len(e))
for i in e:
    print(i.get_attribute("href"))
dr.quit()

#########2、通过css名查找多个元素##########
from selenium import webdriver
dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/")
e=dr.find_elements_by_css_selector("span.sep")
print(len(e))
for i in e:
    print(i.get_attribute("href"))
dr.quit()