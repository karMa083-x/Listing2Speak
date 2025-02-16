from math import prod
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import requests
import numpy as np
from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

def scrape(url):
    try:
        Options=webdriver.ChromeOptions()
        Options.add_argument('headless')
        Options.add_argument('--log-level=1')
        path='C:\Program Files (x86)\chromedriver.exe'
        driver=webdriver.Chrome(path,options=Options)
        driver.get(url)
        details=[]
        title=driver.find_element(By.XPATH,'//*[@id="productTitle"]')

        price=driver.find_element(By.CLASS_NAME,'a-offscreen')
        ratings=driver.find_element(By.XPATH,'//*[@id="reviewsMedley"]/div/div[1]/div[2]/div[1]/div/div[2]/div/span/span')
        
        try:

            desc=driver.find_element(By.ID,'productDescription')
        except NoSuchElementException:
            desc="no Description"
        list=driver.find_element(By.XPATH,'//*[@id="altImages"]/ul')
        li=list.find_elements(By.TAG_NAME,'li')
        numofimgs=0
        numofVideos=0
        for l in li:
            if l.get_attribute('class')=='a-spacing-small item imageThumbnail a-declarative' :
                numofimgs+=1
            elif l.get_attribute('class')=='a-spacing-small item videoThumbnail a-declarative':
                numofVideos+=1
        

        
        details.append(title.text)
        details.append(price.get_attribute('innerHTML'))
        try:
            rank=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[6]/div[15]/div/ul[1]/li/span/text()[1]')
            details.append(rank.text)
        except:
            details.append('n/a')
        details.append(ratings.text)
        details.append(numofimgs)
        details.append(numofVideos)
        if(type(desc) is str):
            details.append(desc)
            details.append(0)
            details.append(0)
        else:
            if(desc.text==''):
                details.append("no description")
                details.append(0)
                details.append(0)
            else:
                details.append(desc.text)
                d=desc.text
                kw=0
                w=0
                keywords=['new', 'smart', 'powerful', 'guide', 'function', 'fun', 'capable', 'makes it easy', 'fast', 'great', 'combine', 'quality', 'incredibly', 'exclusive', 'optimized', 'designed to provide']
                for i in d:
                    if i==" ":
                        w+=1;
                details.append(w)
                for k in keywords:
                    if k in d:
                        kw+=1;
                details.append(kw)
        return details
    except:
        return []


'''
cookies = {'session': '131-1062572-6801905'}
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
data=[]
link='https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_unv_grocery_0_1'
req=requests.get(link,headers=HEADERS)
soup=BeautifulSoup(req.content,'html.parser')
navbar=soup.find_all('div',class_='_p13n-zg-nav-tree-all_style_zg-browse-item__1rdKf _p13n-zg-nav-tree-all_style_zg-browse-height-small__nleKL')

Data=[]




for n in navbar:
    link=n.find('a')['href']
    name=n.find('a').get_text()
    req2=requests.get('https://www.amazon.com'+link,headers=HEADERS)
    soup2=BeautifulSoup(req2.content,'html.parser')
    prods=soup2.find_all('a',class_='a-link-normal')
    Data=[]
    for p in prods:
        link='https://www.amazon.com'+p['href']
        try:
            Data.append(scrape(link))
            
            
        except:
            pass
    try:
        print(Data)
        pd.DataFrame(Data).to_csv(name+'.csv',header=["Name","price","ranking","rating","# of Images","# of videos",'desc',"desc words","keywords"])
    except:
        print('pandas didn"t work')
        print(Data)
'''
        


        

