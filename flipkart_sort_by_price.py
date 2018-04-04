import urllib.request
import bs4 as bs
s=input('what are you searching?')
s=s.replace(" ","%20")
url='https://www.flipkart.com/search?q='+s+'&otracker=start&as-show=on&as=off'
sauce=urllib.request.urlopen(url)
source_code=sauce.read()
soup=bs.BeautifulSoup(source_code,'lxml')
price_list=[]
for tshirt in soup.find_all('div',{'class':'_3liAhj'}):
    title=tshirt.find('a',{'class':"_2cLu-l"})
    price = tshirt.find('div',{'class':'_1vC4OE'})
    item = price.text
    l = list(item)
    del (l[0])
    item = "".join(l)
    price_list.append(item)
l=[]
for i in price_list:
    try:
        it=int(i)
        l.append(it)
    except:
        pass
print(min(l))
