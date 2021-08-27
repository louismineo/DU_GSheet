import re
import bs4
import requests
url = "https://dayuse.sg/s/singapore?selectedAddress=Singapore&sluggableAddress=Singapore"
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; SM-6928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'}
content = requests.get(url,headers=headers)
soup = bs4.BeautifulSoup(content.text,'html.parser')

print(soup.title.string)
print(content.headers)

#PAGE COUNT
pageno_count= []
for pageno in soup.find_all("li",{"class":re.compile('flex-none mx-1')}):
  pageno_count.append(pageno.text)

print(pageno_count)



#CRAWL EACH APGE
import pandas as pd
import numpy as np
links_set=[]
df = pd.DataFrame(columns=[])

for i in pageno_count: 
  pageurl=url+'&page='+i
  content = requests.get( pageurl  , headers = headers)
  soup = bs4.BeautifulSoup(content.text,'html.parser')
  print(pageurl)
  
  #find all the links in href
  test = soup.find_all("a",{"href":re.compile('/hotels/singapore/*')})
  #extract all the href
  links = [i.get("href") for i in test]
  print(str(len(links))+" links on "+pageurl)
  for i in links:
    links_set.append(i)


#print(links_set)
print(len(links_set))
links_set = set(links_set)
#links_set=set(links_set)
print(str(len(links_set)) +" unique links")






#PUSH LIST INTO DF

import pandas as pd
pd.set_option('display.max_colwidth',None)
pd.set_option('display.max_rows',None)
df =pd.DataFrame(links_set,columns=['href'])
df['Avg_$perHr']=""
print(df)


def avgPrice():
    timeslot_list = []
#  for i in range(len(df['href'])):
    url = df['href'][0] #[i]
    content = requests.get(url,headers=headers)
    soup = bs4.BeautifulSoup(content.text,'html.parser')
    print(soup.title.string)

    #GET TIME RANGE
    timeslots = [timeslots.text.strip() for timeslots in soup.find_all('span',"text-2xl py-1 font-light")]
    print(timeslots)
    #CONVERT TIME RANGE TO TIME AND GET THE DIFFERENCE AKA TIMERANGE IN HOURS
    import datetime
    for i in timeslots: datetime.strptime(i,'%I:%M%p')
    print(timeslots)
    #GET PRICES
    prices = [prices.text.strip() for prices in soup.find_all('div',"text-3xl font-extrabold text-right lg:text-left leading-9")]
    print(prices) 
      #timeslot_list.append(time_slots.text)
    #print(timeslot_list)

avgPrice()

    
