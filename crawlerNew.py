#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase
from csv import writer  


#gender of the child
gender=["boy","girl"]

#base url of the site to be scrap
baseUrl="https://www.babynamesdirect.com";

#response for the request form the basr url
response=requests.get(baseUrl);

#html parser for the url soup=>object for the bs4 BeautifulSoup
soup=BeautifulSoup(response.text,'html.parser')

#loocking for the specific details
options=soup.find_all('option')

typeName=[]