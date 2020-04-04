# Import libraries
import requests
# import urllib.request
import urllib
import time
from bs4 import BeautifulSoup	# only works in Python2
#############################################################################################
#############################################################################################
#############################################################################################
# WARNING: The files being downloaded here, are too big in size. So just don't do this
#############################################################################################
#############################################################################################
#############################################################################################
# Set the URL you want to webscrape from
url = 'http://web.mta.info/developers/turnstile.html'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
for i in range(36,len(soup.findAll('a'))+1): #'a' tags are for links
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    download_url = 'http://web.mta.info/developers/'+ link
	# in python2 like this: urllib.urlretrieve 
    urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 
	### veya: # only works in Python2
	# filedata = urllib2.urlopen('http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg')
	# datatowrite = filedata.read()
	# with open('cat.jpg','wb') as f:
	# 	f.write(datatowrite)
	### veya:
	# r = requests.get(url)
	# with open('cat3.jpg', 'wb') as f:
		# f.write(r.content)
	# extra info:
	# print(r.status_code)
	# print(r.headers['content-type'])
	# print(r.headers['Content-Length'])	# file size. it may not exist sometimes
	# print(r.encoding)
    time.sleep(1) #pause the code for a sec
	
	