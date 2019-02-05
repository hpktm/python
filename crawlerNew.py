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



#filtering data
for option in options:
	category=option.get_text();
	if(category!='Category'):
		if(category!='Contains'):
			if(category!='Starting from'):
				if(category!='Ends with'):
					str1=option.get_text();
					typeName.append(str1);


typeName=typeName[:len(typeName)//2]
				
# new url for crawler
nameUrl=baseUrl+"/baby-names";


urls=[];
finalUrl=[];

#creating distinct url for to scrapp full site 
for typ in typeName:
	for g in gender:
		for c in ascii_lowercase:
			actualUrl=nameUrl+'/'+typ+'/'+g+'/'+c;
			urls.append(actualUrl);
			

def scrapper(url):
		i=0
		response=requests.get(url);
		soup=BeautifulSoup(response.text,'html.parser')
		data=soup.find_all(class_='nvar')
		crawler=soup.find("nav",attrs={"class":"pages"})
		
		for a in crawler:
			href=a.get('href')
			print(href)

		#scrapper(crawler);

		# with open('post.csv','a') as csv_file:
		# 	csv_writer=writer(csv_file)
		# 	headers=['Names']
		# 	csv_writer.writerow(headers)

		# 	for d in data:
		# 		name=d.get_text();
		# 		csv_writer.writerow([name])

			
				


for url in urls:
	scrapper(url);
	break;
