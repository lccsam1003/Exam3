# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url='https://rate.bot.com.tw/xrt?Lang=zh-TW'

page=requests.get(url)

bsObj=BeautifulSoup(page.content,'html.parser')

#print(bsObj)


for tr in bsObj.find('table').find('tbody').findAll('tr'):
    
    #print(tr)
    
    cell=tr.findAll('td')
    
    #print(cell[1])
    
    currency=cell[0].find('div',{'class':'visible-phone'}).contents[0]
    #print(currency)
    
    currency=currency.replace('\r','')
    currency=currency.replace('\n','')   
    currency=currency.replace(' ','')
    
    #print(currency)
    
    curr_rate=cell[2].contents[0]
    
    print(currency,':',curr_rate)
    
    
    
    
    