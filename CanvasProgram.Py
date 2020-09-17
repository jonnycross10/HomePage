from canvasapi import Canvas
from secrets import url,apiKey

canvas = Canvas(url,apiKey)

usr = canvas.get_current_user()

l = usr.get_courses()

for i in range(0,3):
  print(l[i])
  for n in l[i].get_assignments():
    print(n, "\n")

