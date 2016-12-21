# -*- coding: utf-8 -*-
import requests
import lxml
import os
import io
import time
from bs4 import BeautifulSoup
output = ""
while(1):
    place = raw_input("Place:\n")
    if place == '':
        break
    url = raw_input("URL:\n")
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')
    output += place + soup.html.head.title.string[:-8] + '\n' + url + '\n'
print (time.strftime("%Y/%m/%d"))
print "工商時報"
print output
