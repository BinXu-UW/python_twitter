# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 20:30:19 2018

@author: Binkowsky
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='D:\....\chromedriver.exe')
#添加自己的chromedriver的环境变量
#driver.maximize_window()


driver.get('https://twitter.com/login')
time.sleep(3)

driver.find_element_by_class_name('js-username-field').clear()# 选择用户名框
driver.find_element_by_class_name('js-username-field').send_keys('xxxxxxx@gmail.com')#Twitter 账户


driver.find_element_by_class_name('js-password-field').clear()
driver.find_element_by_class_name('js-password-field').send_keys('xxxxxxxxx')#twitter 密码

#driver.find_element_by_id('login_button').click()
driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium').submit()
time.sleep(3)
#睡眠时间很重要，得等网页打开
search_box=driver.find_element_by_id("search-query")
keyword="#Flu2018"
search_box.send_keys(keyword)
driver.find_element_by_css_selector('button.Icon.Icon--medium.Icon--search.nav-search').submit()


#driver.get('https://user.qzone.qq.com/{}'.format('xxxxx')) #你盆友的QQ号
#time.sleep(3)
#html = driver.page_source
#soup = BeautifulSoup(html,'lxml')
#a = soup.find_all('div',{'class':'f-info'})
#
#f=open('test1.txt','w')
#
#for i in range(len(a)):
#    f.write(a[i].text+'/n')
#    #print(a[i].text)
