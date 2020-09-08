#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# from selenium import webdriver
# import os
# dr=webdriver.Firefox()
# dr.get('file:///'+os.path.abspath('HTML02/09HTML.html'))
# # e=dr.find_elements_by_xpath("//input[@name='cin']")
# # e=dr.find_elements_by_xpath("//form[@id='loginForm']/input")
# e=dr.find_elements_by_xpath("//*[@name='cin']")
# print(len(e))
# print(e[0].get_attribute('type'))
# print(e[1].get_attribute('type'))
# dr.quit()

'''
1./html/body/form[1] --该路径下第一个form
2.//form[1] --html下第一个form
4.//form[input/@name='username'] --form里有input,input里的属性name是叫username的,第一个form,找的是form
7.//input[@name='continue'][@type='submit'] --type属性为'submit',name属性为'continue'的第一个input元素
'''
from selenium import webdriver
import os
dr=webdriver.Firefox()
dr.get('file:///'+os.path.abspath('xpath-案列.html'))
# e=dr.find_elements_by_xpath("/html/body/form")
e=dr.find_elements_by_xpath("//form[input/@name='maker']")
print(len(e))
# print(e[0]._getattribute__("type"))
for i in e:
    print(i.get_attribute('type'))
dr.quit()