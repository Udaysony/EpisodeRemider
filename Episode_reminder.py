import urllib.request as ul
import bs4 as bs
import datetime


favourite_episodes = ["the big bang theory", "gotham","the flash"]  #Enter your favourite episode in list
l = []

tv_url = 'http://www.tvmaze.com'

page = ul.urlopen(tv_url).read()

soup = bs.BeautifulSoup(page,'lxml')

for names in soup.find_all("span", {"class": "showname"}):
	l.append(names.text)			#creates list of todays episodes

for i in favourite_episodes:
	if i.title() in l:
		print("{} is going to air today".format(i)) # we can call a function which can send text reminder
	

