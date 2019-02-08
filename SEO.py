# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 17:06:50 2019

@author: Leonard
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = input("Which page wuld you like to check? Enter Full URL: ")
keyword = input("What is you seo keyword")
keyword = keyword.casefold()

try:
    html = urlopen(url)
except HTTPError as e:
    print(e)
    
data = BeautifulSoup(html,"html.parser")

def seo_title_found(keyword,data):
    if data.title:
        
        if keyword in data.title.text.casefold():
            status = "Found"
        else:
            status = "Keyword Not Found"
    else:
       status = "No title Found"
       
    return status

#Search engine wont crawl over these words
def seo_title_stop_words(data): 
    words = 0
    list_words =[]
    if data.title:
        with open('stopwords.txt','r') as f:
            for line in f:
                if re.search(r'\b'+line.rstrip('\n') + r'\b', data.title.text.casefold()):
                    words += 1
                    list_words.append(line.rstrip('\n'))
        if words > 0 :
            stop_words = "We Found {} stop words in your title. {}".format(words,list_words)
        else:
            stop_words = "We found no stop words in the title"
    else:
        stop_words = "We could not find a title"
    return stop_words
        

print(seo_title_found(keyword,data))
print(seo_title_stop_words(data))