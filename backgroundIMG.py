#http://www.7timer.info/bin/astro.php?lon=38&lat=121&ac=0&unit=metric&output=json&tzshift=0
import requests
import json
from secrets import lat,lon 
import socket
from ipgeo import ipgeo
from PIL import Image
from datetime import datetime


info = ipgeo.query('182.138.127.93')
#print(info.latitude)

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(ip_address)




#lat = "38.81"
#lon = "-121.27"
urlString = "http://www.7timer.info/bin/api.pl?lon=" + lon + "&lat=" + lat + "&product=civil&output=json"

# "http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=civil&output=json"


#r = requests.get("http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=civil&output=json")

r = requests.get(urlString)

#print(r.text)
x = {}
x = json.loads(r.text)
print(x['dataseries'][0]['weather'])

im = Image.open("imgs/" + str(datetime.today().weekday()) + ".jpg")

im.save("todaysImg.jpg")
