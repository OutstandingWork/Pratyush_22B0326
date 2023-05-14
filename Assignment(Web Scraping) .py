import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
url="https://itc.gymkhana.iitb.ac.in/wncc/soc/"
response=requests.get(url)
# text=response.text
soup=BeautifulSoup(response.text,'html.parser')
c=0
links = []
for link in soup.find_all('a'):
    href = link.get('href')
    links.append(href)
    
my_link=[]
for link in links:
    if(link is not None and link.startswith("/wncc/soc/projects/2023/")):
        my_link.append((link.replace('/wncc/soc/',"")))
        
for i in my_link:
    c=c+1
    
    

mentor1=[]
mentee1=[]
mentor_n=[]
project_name=[]
link=[]

for i in range(c):
    url1=url+my_link[i]
    response1=requests.get(url1)
    soup1=BeautifulSoup(response1.text,"html.parser")
    mentor=soup1.find('h4',class_="display3").next_sibling.next_sibling.text
    c1=0
    for j in mentor:
     if(j=="\n"):
            c1=c1+1
    mentor_n.append(c1-1)
    mentor=(soup1.find('h4',class_="display3").next_sibling.next_sibling.text).strip("\n").replace("\n",",")
    mentee_n=(soup1.find('h4',class_="display3").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text).replace("\n","")
    proj_name=(soup1.find('h2',class_="display1 m-3 p-3 text-center project-title").text.replace("/n","")).replace("\n","")
    mentor1.append(mentor)
    mentee1.append(mentee_n)
    project_name.append(proj_name)
    link.append(url+my_link[i])
    
    


   


    
    
    
dict1={"Name of mentor":mentor1,"Number of Mentor":mentor_n,"Number of mentee":mentee1,"Project name":project_name,"Project Link":link}
df=pd.DataFrame(dict1,index=range(1,72))
df.index.name="Index"
df.to_excel("Assignment.xlsx")