import pandas as pd
df = pd.read_csv('df.csv')
df['timeRangeInHrs'] = ""
df['priceInDollars'] = ""

print(df)

def avgPrice():
    timeslot_list = []
#  for i in range(len(df['href'])):
    #url = df['href'][0] #[i]
    url = "https://dayuse.sg/hotels/singapore/hotel-nuve-steller"
    content = requests.get(url,headers=headers)
    soup = bs4.BeautifulSoup(content.text,'html.parser')
    print(soup.title.string)

    #GET TIME RANGE
    timeslots = [timeslots.text.strip() for timeslots in soup.find_all('span',"text-2xl py-1 font-light")]
    print(timeslots)
    #GET PRICES
    prices = [prices.text.strip() for prices in soup.find_all('div',"text-3xl font-extrabold text-right lg:text-left leading-9")]
    print(prices)
    #timeslot_list.append(time_slots.text)
    #print(timeslot_list)


def timerange(string):
  from datetime import datetime 
  start=datetime.strptime(string.split(" - ")[0],'%I:%M %p')
  end = datetime.strptime(string.split(" - ")[1],'%I:%M %p')
  timediff = end - start
  timediff = timediff.total_seconds()/3600
  print(timediff)
  return timediff

def getIntegers(string):
    price = int(filter(str.isdigit, string))
    return price



#loop thru all the rows in df
for i in range(len(df)):
    #MAKE LIST OF TIME RANGES
    timerange_list=[]
    for timeslot in df['timeslots'][i]:
        timerange_list.append(timerange(timeslot))
    
    #MAKE LIST OF PRICES IN INT W.O THE 'SGD' STRING
    pricesInt_List=[]
    for prices in df['prices'][i]:
        pricesInt_List.append(getIntegers(prices))
    
    df['timeRangeInHrs'][i] = timerange_list
    df['priceInDollars'][i] = pricesInt_List

