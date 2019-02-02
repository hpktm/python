#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from csv import writer  

response=requests.get('https://www.babynamesdirect.com/baby-names/indian/boy/a')
soup=BeautifulSoup(response.text,'html.parser')

posts=soup.find_all(class_='nvar')


with open('post.csv','w') as csv_file:
	csv_writer=writer(csv_file)
	headers=['names']
	csv_writer.writerow(headers)

	for post in posts:
		name=post.get_text();
		csv_writer.writerow([name])