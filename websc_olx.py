# encoding=utf8
import urllib2
from urllib2 import urlopen 
import time
from bs4 import BeautifulSoup
import json
import pandas as pd




URL = 'https://www.olx.in/bengaluru_g4058803/computers-laptops_c1505/q-laptop'
soup = BeautifulSoup(urlopen(URL),"lxml")




#links = soup.findAll('div')
#print(links)
# Take out the <div> of name and get its value
#print soup

#name_box = soup.find('span', attrs={'class': '_89yzn'})
#name_box = name_box.text
#print name_box

products=[] #List to store name of the product
prices=[] #List to store price of the product
url=[] #List to urls of the product
Arr = []

# Loop thru all the Laptops

for a in soup.findAll('li', attrs={'class':'EIR5N'}):
        name=a.find('span', attrs={'class':'_2tW1I'})
        name = (name.text.encode("utf-8"))
        price=a.find('span', attrs={'class':'_89yzn'})
        price = price.text.encode("utf-8")
        link = a.find('a').get('href')
        link = str ('https://www.olx.in') + link
     #   ln = link.get('href') 
#        link = a.attrs['href']
        print (link)
        url.append(link) 
        products.append(name)
        prices.append(price)
        jobj = { "Name" : name ,
                 "Price" : price,
                 "url" : link
               }
        Arr.append(jobj)
        print (Arr)
# Write to Json
        with open('laptopsData.json', 'w') as outfile:
          json.dump(Arr, outfile)

# Write to CSV
df = pd.DataFrame({'Product Name':products,'Price':prices,'links':url}) 
df.to_csv('laptops.csv', index=False, encoding='utf-8')
#df.to_json('laptops.json', orient='records', lines=True)
print ("completed")
