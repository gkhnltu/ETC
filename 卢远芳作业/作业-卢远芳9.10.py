#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
# 一．今天的代码敲一遍
# 二．页面滚动条，做成缓慢下拉的动画效果
"""

from selenium import webdriver
import time

dr=webdriver.Firefox()
dr.get("https://www.hao123.com/")
# js="document.documentElement.scrollTop=10000"
# dr.execute_script(js)
dr.set_window_size(400,600)
for i in range(30):
        js='window.scrollBy(0,100)'
        dr.execute_script(js)
        time.sleep(0.5)
"""
# 三．登入电商系统，然后添加收件地址，然后退出电商系统，每个用例都写成模块化。
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


def login(dr):
    sleep(4)
    dr.find_element_by_link_text("登陆").click()
    sleep(2)
    dr.find_element_by_id("username").send_keys("list_12")
    sleep(2)
    dr.find_element_by_id("password").send_keys("123456")
    sleep(2)
    dr.find_element_by_link_text("登     陆").click()
    sleep(4)

def add(dr):

    sleep(8)
    dr.find_element_by_link_text("收件地址").click()
    sleep(4)
    dr.find_element_by_id("newadrbtn").click()
    sleep(4)
    dr.find_element_by_id("receiver").send_keys("小卢")
    sleep(3)
    e=dr.find_element_by_id("areaslt-province")
    sleep(2)
    listobj=Select(e)
    listobj.select_by_visible_text('湖北省')
    sleep(2)

    # listobj.select_by_index(12)
    e=dr.find_element_by_id("areaslt-city")
    listobj=Select(e)
    listobj.select_by_visible_text('武汉市')
    sleep(2)

    e=dr.find_element_by_id("areaslt-borough")
    listobj=Select(e)
    listobj.select_by_visible_text("江岸区")
    sleep(2)

    dr.find_element_by_id("address").send_keys("幸福大街")
    sleep(2)
    dr.find_element_by_id("zip").send_keys("100300")
    sleep(2)
    dr.find_element_by_id("mobile").send_keys("13545770903")
    sleep(2)
    dr.find_element_by_css_selector("button.sm-green").click()
    sleep(2)

def logout(dr):
    sleep(10)
    e = dr.find_element_by_xpath('//*[@id="top-userbar"]/a')
    sleep(2)
    ActionChains(dr).move_to_element(e).perform()
    sleep(2)
    dr.find_element_by_link_text('退出').click()

dr=webdriver.Firefox()
dr.get("http://39.96.181.61/qftest-ds/")
login(dr)
add(dr)
logout(dr)
dr.quit()
"""
# 四．把注册功能写成模块化
from selenium import webdriver
from time import sleep
import csv
import time

# with open("2.csv","a",encoding="utf-8",newline="")as f1:
#     dd=csv.writer(f1)
#     dd.writerow(['','','http://39.96.181.61/qftest-ds/user/index.html'])
#     print(dd)

with open("2.csv","r",encoding="utf-8") as f:
    cc=csv.reader(f)
    mylist=[]
    for i in cc:
        mylist.append(i[2])
    print(mylist)
#
dr=webdriver.Firefox()
# 打开网站
dr.get('http://39.96.181.61/qftest-ds/')
time.sleep(2)
# 获取免费注册元素并点击
dr.find_element_by_link_text('免费注册').click()
time.sleep(3)
# 获取用户名输入框,并输入数据
dr.find_element_by_id('username').send_keys(mylist[0])
time.sleep(2)
# 获取邮箱输入框,并输入数据
dr.find_element_by_id('email').send_keys(mylist[1])
time.sleep(2)
# 获取密码输入框,并输入数据
dr.find_element_by_id('password').send_keys(mylist[2])
time.sleep(2)
# 获取确认密码输入框,并输入数据
dr.find_element_by_id('repassword').send_keys(mylist[3])
time.sleep(2)
# 获取'立即注册'元素,并点击
dr.find_element_by_link_text('立即注册').click()

time.sleep(9)

# 获取断言的url
url=mylist[4]

if dr.current_url == url:
    print("注册成功")
else:
    print("注册失败")

time.sleep(2)

dr.quit()