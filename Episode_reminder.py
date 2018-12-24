

#  Script has to run manually for now. We can make a job_script to run it on specific time, everyday. 
# Edit yyour faviourite episodes in list to get notifications.

import urllib.request as ul
import bs4 as bs
import datetime
import smtplib



favourite_episodes = ["the big bang theory", "gotham"]  #Enter your favourite episode in list
l = []

tv_url = 'http://www.tvmaze.com'

page = ul.urlopen(tv_url).read()

soup = bs.BeautifulSoup(page,'lxml')

for names in soup.find_all("span", {"class": "showname"}):
	l.append(names.text)			#creates list of todays episodes

sender = "abc@gmail.com"	
password = "password"
target = "xyz"

server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.ehlo()
server.login(sender,password)


for i in favourite_episodes:
	if i.title() in l:
		msg = i + " is going to air today." 
		server.sendmail(sender,target,msg)

	
server.quit()

