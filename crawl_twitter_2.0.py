# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 20:30:19 2018

@author: Binkowsky
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path='D:\chromedriver_win32\chromedriver.exe')
#添加自己的chromedriver的环境变量 Add your chromedriver Environment Variabeles
#driver.maximize_window() ##Change window size

#%% Login and Search key words
driver.get('https://twitter.com/login')
time.sleep(3) #sleep is important or you won't be able to login

driver.find_element_by_class_name('js-username-field').clear()# 选择用户名框 clear the username box
driver.find_element_by_class_name('js-username-field').send_keys('xxxxxxxx@gmail.com')#Twitter 账户 Yor username


driver.find_element_by_class_name('js-password-field').clear()# clear the password box
driver.find_element_by_class_name('js-password-field').send_keys('xxxxxxx')#twitter 密码 password

#driver.find_element_by_id('login_button').click()
driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium').submit()
#click the login in buttton
time.sleep(3)

search_box=driver.find_element_by_id("search-query")
keyword="#Flu2018"
search_box.send_keys(keyword)
driver.find_element_by_css_selector('button.Icon.Icon--medium.Icon--search.nav-search').submit()


#%% Collecting tweets form the webpage
import datetime as dt

html = driver.page_source
soup = BeautifulSoup(html,'lxml')

tweets = soup.findAll('li',{"class":'js-stream-item'})

for tweet in tweets:
    if tweet.find('p',{"class":'tweet-text'}):
        tweet_user = tweet.find('span',{"class":'username'}).text.strip()
        tweet_text = tweet.find('p',{"class":'tweet-text'}).text.encode('utf8').strip()
        tweet_id = tweet['data-item-id']
        timestamp = tweet.find('a','tweet-timestamp')['title']
        tweet_timestamp = dt.datetime.strptime(timestamp, '%H:%M - %d %b %Y')
        #replies = tweet.find('span',{"class":"ProfileTweet-actionCount"}).text.strip()
        #retweets = tweet.find('span', {"class" : "ProfileTweet-action--retweet"}).text.strip()
        ## You can collect retweets if you want
        print(tweet_user)
        print(tweet_text)
        print(tweet_id)
        print(timestamp)
        print(tweet_timestamp)
        #print(replies)
        #print(retweets)
    else:
        continue


#f=open('collecting_twitter.txt','w')
#
#for i in range(len(a)):
#    f.write(a[i].text+'/n')
#    print(a[i].text)
