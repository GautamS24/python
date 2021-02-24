import requests
import urllib3
from bs4 import BeautifulSoup

URL='https://vscrm.in/'
page=requests.get(URL)
soup=BeautifulSoup(page.text,'html.parser')
#print(soup.text)
#title=soup.find('title')
# qwery=soup.find('h1')
q2=soup.findAll('meta')
# content
#contents=soup.findAll("meta",class_='name')
for i in q2:
   print(i)

links=soup.findAll('a')
#print(links)
#print(links['class'])
#e1=len(links)
for i in links:
   print(i)
# print(q2)
# print(q2['content'])
# for i in q2[:6]:
    #print(i)
# print(e1)
#print(links['href'])
