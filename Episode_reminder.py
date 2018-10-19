import urllib.request as ul
import bs4 as bs
import datetime
import re

l = []
tv_url = 'http://www.tvmaze.com'

page = ul.urlopen(tv_url).read()

soup = bs.BeautifulSoup(page,'lxml')

for names in soup.find_all("span", {"class": "showname"}):
	l.append(names.text)			#creates list of todays episodes

while True:

	input_ep = input("press y for todays list or press n to search for specific episode(y/n):")


	if input_ep == "y":
		print(l)
		exit()
	elif input_ep == "n":
		search_ep = input("Episode name: ")
		print( "yes" if search_ep.title() in l else "not on air today") #searches your desired input in list
		exit()
	else:
		print("Please enter valid input")


