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

typeName=[];


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

for url in urls:
	response=requests.get(url)
	soup=BeautifulSoup(response.text,'html.parser')

	try:
		el=soup.find('small').get_text();
	except:
		continue
	
	upperLimit=el.split(' ')
	Ul=int(upperLimit[3])

	i=0;

	while(Ul):
		i=i+1;
		activeUrl=url+'/'+str(i)
		finalUrl.append(activeUrl)
		Ul=Ul-1
		

print(finalUrl)

	# 	crawler=requests.get(activeUrl)
	# 	data=BeautifulSoup(crawler.text,'html.parser')
		
	# 	posts=soup.find_all(class_='nvar')
		
	# 	with open('a1.csv','w') as csv_file:
	# 			csv_writer=writer(csv_file)
	# 			for post in posts:
	# 				name=post.get_text();
	# 				csv_writer.writerow([name])
	# 	Ul=Ul-1# while  loop decrement


	# break;#for "for" loop to end		


	








