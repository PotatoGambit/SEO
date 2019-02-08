# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 17:06:50 2019

@author: Leonard
"""

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

url = input("Which page wuld you like to check? Enter Full URL: ")
keyword = input("What is you seo keyword: ")
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

#title length no larger than 60 characters

def seo_title_length(data):
    if data.title:
        if len(data.title.text) < 60:
            length = "Your length is under the maximum suggested length. YOur title is {}".format(len(data.title.text))
        else:
            length = "YOur length is over the max.{}".format(len(data.title.text))
    else:
        length = "NO TITLE FOUND"
    
    return length

# Keyword should appear in URL

def seo_url(url):
    if url:
        if keyword in url:
            slug = "your keyword was found in your slug"
        else:
            slug = "Keyword not found in slug"
    else:
        slug = "No url was returned"
    return slug

def seo_url_length(url):
    if url:
             if len(url) < 100:
                 url_length = " Your URL length is less than than the 100 character maximum @ {}".format(len(url))
             else:
                 url_length = "YOur URL length is over 100 characters @ {}".format(len(url))
    else:
        url_length = "No url found"
    
    return url_length

def seo_h1(keyword,data):
    total_h1 = 0
    total_keyword_h1 = 0
    
    if data.h1:
        all_tags = data.find_all('h1') #BS4 find all tags.
        for tag in all_tags:
            total_h1 += 1
            tag = str(tag.string)
            if keyword in tag.casefold():
                total_keyword_h1 += 1
                h1_tag = "Found keyword in h1 tag.You have a total of {} H1 Tags and your keyword was found in {} of them".format(total_h1, total_keyword_h1 )
            else:
                h1_tag = "Did not find a keyword in h1 tag."
        
    else:
        
        h1_tag = "No h1 tags found"
    
    return h1_tag
    
         

print(seo_title_found(keyword,data))
print(seo_title_stop_words(data))
print(seo_title_length(data))
print(seo_url(url))
print(seo_url_length(url))
print(seo_h1(keyword,data))
