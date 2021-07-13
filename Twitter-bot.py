'''
!!!IMPORTANT READ!!!
This code may not work when you run it and it's because one of the classes we called may have changed,
'''

import time

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#Starts the driver and goes to our starting webpage
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

driver.get('https://twitter.com/login')
time.sleep(2)
 
#   put your fav celebrity name here ....   
celebrity = 'Ryan Reynolds'

login = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
login.send_keys('your email ')
password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
password.send_keys('your password ')


button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div').click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')))

search = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
search.send_keys(celebrity)
search.send_keys(Keys.ENTER)
time.sleep(2)

people = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div').click()
time.sleep(2)


profile = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a/div/div[1]/div[1]/span').click()
time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'lxml')


postings = soup.find_all('div', class_ = 'css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0') 


tweets = []
while True:
    for post in postings:
        tweets.append(post.text)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    #need to change the class here to match it with the other posting variable if there is an error
    postings = soup.find_all('div', class_ = 'css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0')
    tweets2 = list(set(tweets))
    if len(tweets2) > 500:
        break



new_tweets = []    
for i in tweets2:
   
    if '' in i:
        new_tweets.append(i)

df = pd.DataFrame(new_tweets)
df.to_csv('all_data.csv',index = False)


# done/////////////////////////////////////////////////////////////////////////// 
    
        












