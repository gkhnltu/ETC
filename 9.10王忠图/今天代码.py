#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import csv

# dr=webdriver.Firefox()
# dr.get("https://www.qq.com")
# dr.find_element_by_link_text('Qmail').click()
# hs=dr.window_handles
# dr.switch_to.window(hs[1])
# sleep(2)
# iframeObj=dr.find_element_by_xpath('//*[@id="login_frame"]')
# dr.switch_to.frame(iframeObj)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('12345678')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('123456')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
# dr.switch_to.default_content()
# dr.find_element_by_link_text('基本版').click()
# sleep(2)
# dr.quit()

# dr=webdriver.Firefox()
# dr.get("https://www.baidu.com")
# dr.maximize_window()
# e=dr.find_element_by_tag_name('span')
# ActionChains(dr).move_to_element(e).perform()
# sleep()
# dr.find_element_by_link_text('搜索设置').click()
# sleep(3)
# dr.find_element_by_id('nr_2').click()
# sleep(4)
# dr.find_element_by_link_text("保存设置").click()
# dd=dr.switch_to.alert
# dr.quit()

# dr=webdriver.Firefox()
# sleep(3)
# dr.get('https://www.baidu.com')
# dr.find_element_by_id('kw')
#
# try:
#     ele=WebDriverWait(dr,5,0.5,ignored_exceptions=None).until(EC.presence_of_element_located((By.ID,'kw')),"找不到")
#     ele.send_keys('selenium')
#     sleep(3)
# except:
#     print(sys.exc_info())

# dr=webdriver.Firefox()
# dr.get('https://www.hao123.com/')
# dr.set_window_size(400.400)
# sleep(3)
# js="document.documentElement.scrollTop=10000"
# dr.execute_script(js)
# sleep(2)
# js="window.scrollTo(100,200)"
# dr.execute_script(js)
# sleep(2)
# dr.quit()



# #打开网站
# dr.get("http://39.96.181.61/qftest-ds/")
#
# #获取免费注册元素并点击
# dr.find_element_by_link_text('免费注册').click()
# sleep(3)
# #获取用户名输入框,并输入数据
# dr.find_element_by_id('username').send_keys('gggkv123')
# sleep(3)
# #获取邮箱输入框,并输入数据
# dr.find_element_by_id('email').send_keys('ascvve@qq.com')
# sleep(3)
# #获取密码输入框,并输入数据
# dr.find_element_by_id('password').send_keys('12345678')
# sleep(3)
# #获取确认密码输入框,并输入数据
# dr.find_element_by_id('repassword').send_keys('12345678')
# #获取'立即注册'元素,并点击
# dr.find_element_by_link_text('立即注册').click()
# sleep(10)
# #获取当前页面的url
# aa=dr.current_url
# #进行判断http://39.96.181.61/qftest-ds/user/index.html
# if aa=='http://39.96.181.61/qftest-ds/user/index.html':
#     print('注册成功')
# else:
#     print('注册不成功')
# #关闭浏览器
# dr.quit()

# def Acc(dr):
#     dr.find_element_by_link_text('登陆').click()
#     sleep(2)
#     dr.find_element_by_id('username').send_keys('ggkk123')
#     sleep(1)
#     dr.find_element_by_id('password').send_keys('123456')
#     sleep(1)
#     dr.find_element_by_link_text('登     陆').click()
#     sleep(8)
#
# def cad(dr):
#     #获取退出登入元素,并点击
#     dr.find_element_by_link_text('退出登录')
# if __name__=='__main__':
#     dr=webdriver.Firefox()
#     dr.get('http://39.96.181.61/qftest-ds/')
#     sleep(2)
#     Acc(dr)
#     sleep(5)
#     cad(dr)
#     sleep(5)
#     dr.quit()

with open("01.csv","r",encoding='utf-8') as f:
    d=csv.reader(f)
    m=[]
    for i in d:
        m.append(i[0])
        print(m)
    dr=webdriver.Firefox()
    dr.get('http://39.96.181.61/qftest-ds/')
    sleep(2)
    dr.find_element_by_link_text('免费注册').click()
    sleep(3)
    dr.find_element_by_id('username').send_keys(m[0])
    sleep(2)
    dr.find_element_by_id('email').send_keys(m[1])
    sleep(2)
    dr.find_element_by_id('password').send_keys(m[2])
    sleep(2)
    dr.find_element_by_id('repassword').send_keys(m[3])
    sleep(2)
    dr.find_element_by_link_text('立即注册').click()
    sleep(9)
    myurl=m[4]
    if dr.current_url==myurl:
        print('ok')
    else:
        print('No')
    sleep(2)
    dr.quit()























































