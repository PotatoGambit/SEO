# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 17:06:50 2019

@author: Leonard
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("Which page wuld you like to check? Enter Full URL: ")
keyword = input("What is you seo keyword")

try:
    html = urlopen(url)
except HTTPError as e:
    print(e)
    
data = BeautifulSoup(html,"html.parser")

def seo_title(keyword,data):
    if keyword.casefold() in data.title.text.casefold():
        status = "Found"
    else:
        status = "Not Found"
    return status

print(seo_title(keyword,data))