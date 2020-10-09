from datetime import date

#get today's date as a number
d = date.today()
today = d.weekday()

img = "https://ghchart.rshah.org/"
color = ["ffff00","ffc0cb","008000","ffa500","409ba5","800080","ff0000"]

#assign the color of the day to the variable
todaysColor = color[today]

#assemble the url string with the color and my github id
urlString = "https://ghchart.rshah.org/" + todaysColor +"/jonnycross10"

#make a javascript file and give it the correct url to give to html
f = open("mapMake.js", "w")
f.write("var urlString = \"" + urlString +"\";\ndocument.getElementById('map').src = urlString;")
f.close()
