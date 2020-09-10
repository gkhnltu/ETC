#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from selenium import webdriver
from time import sleep

def Ass(a1,a2,a3):#a1用户名，a2邮箱，a3密码。
    dr=webdriver.Firefox()
    dr.get("http://39.96.181.61/qftest-ds/")
    dr.find_element_by_link_text('免费注册').click()
    sleep(3)
    dr.find_element_by_id('username').send_keys(a1)
    sleep(3)
    dr.find_element_by_id('email').send_keys(a2)
    sleep(3)
    dr.find_element_by_id('password').send_keys(a3)
    sleep(3)
    dr.find_element_by_id('repassword').send_keys(a3)
    sleep(3)
    dr.find_element_by_link_text('立即注册').click()
    sleep(8)
    aa = dr.current_url
    if aa == 'http://39.96.181.61/qftest-ds/user/index.html':
        print('注册成功')
    else:
        print('注册不成功')
    dr.quit()

Ass('ggkk123','gggkk@qq.com','123456')
