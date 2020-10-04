#this program will be responsible for selecting the website's background
import requests
import json
from secrets import lat,lon
import socket
from ipgeo import ipgeo #pip install ipgeo
from PIL import Image #pip install pillow

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(ip_address)


urlString = "http://www.7timer.info/bin/api.pl?lon=" + lon + "&lat=" + lat + "&product=civil&output=json"


r = requests.get(urlString)

#put the weather info into a dict and print out today
x = {}
x = json.loads(r.text)
print(x['dataseries'][0]['weather'])

#open image in folder and save it as background image in current file
im = Image.open("imgs\saturday.jpg")
im.save("background.jpg", "JPEG")

#later i will select the picture based on the day of the week
#after that I will add pictures to be selected depending on 
#the weather and time of day as well
