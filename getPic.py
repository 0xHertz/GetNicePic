# coding=utf-8
# 2021.3.16

import os
import requests
import re
from bs4 import BeautifulSoup
from bs4 import element
import csv
from requests.api import get
from requests.exceptions import RequestsDependencyWarning

from requests.models import Response


base = 'https://yomoi.myportfolio.com'
tar = "https://yomoi.myportfolio.com/work"

def getLink():
    listtar = []
    response = requests.get(tar)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, 'lxml')
    for link in soup.find('section',{'class':"project-covers"}).find_all('a',):
        listtar.append(base + str(link['href']))


    getPic(listtar)

def getPic(listtar):
    for tmptar in listtar:
        response = requests.get(tmptar)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, 'lxml')
        
        # print(soup)
        soup = soup.find('div', {'class':'project-module module media_collection project-module-media_collection'})
        # print(soup)
        print("Pic***************************************")
        imgs = soup.find_all('img',)
        i = 0
        srcs = []
        for img in imgs:
            # print(img['src'])
            try:
                img = str(img['data-src']).split("?")[0]
            # i += 1
            # if img[0] == '/':
            #     img = "http://society.people.com.cn" + img
                print(img)
                srcs.append(img)
            except:
                img = str(img['src']).split('?')[0]
                # print(img)
                srcs.append(img)
        for src in srcs:
            result = requests.get(src)
            # print(src.split('/')[-1])
            with open(str(src[-28:]),"wb") as f:
                f.write(result.content)

getLink()
