#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


def Acc(dr):
    dr.find_element_by_link_text('登陆').click()
    sleep(2)
    dr.find_element_by_id('username').send_keys('ggkk123')
    sleep(1)
    dr.find_element_by_id('password').send_keys('123456')
    sleep(1)
    dr.find_element_by_link_text('登     陆').click()
    sleep(8)
    dr.find_element_by_link_text("收件地址").click()
    sleep(4)
    dr.find_element_by_id("newadrbtn").click()
    sleep(1)
    dr.find_element_by_id("receiver").send_keys('小王')
    sleep(2)
    e=dr.find_element_by_id('areaslt-province')
    listobj=Select(e)
    listobj.select_by_visible_text("广东省")
    sleep(1)
    e=dr.find_element_by_id('areaslt-city')
    listobj = Select(e)
    listobj.select_by_visible_text("深圳市")
    sleep(1)
    e=dr.find_element_by_id('areaslt-borough')
    listobj = Select(e)
    listobj.select_by_visible_text("宝安区")
    sleep(1)
    dr.find_element_by_id('address').send_keys("深圳市宝安区钟屋新村")
    sleep(1)
    dr.find_element_by_id('zip').send_keys('123456')
    sleep(1)
    dr.find_element_by_id('mobile').send_keys('13845678910')
    sleep(1)
    dr.find_element_by_class_name('sm-green').click()
    sleep(8)
    a=dr.find_element_by_xpath('//*[@id="top-userbar"]/a')
    ActionChains(dr).move_to_element(a).perform()
    sleep(1)
    dr.find_element_by_link_text('退出').click()

if __name__=='__main__':
    dr=webdriver.Firefox()
    dr.get("http://39.96.181.61/qftest-ds/")
    Acc(dr)
    dr.quit()
