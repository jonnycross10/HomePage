from canvasapi import Canvas
from Secrets import url,apiKey

canvas = Canvas(url,apiKey)

usr = canvas.get_current_user()

l = usr.get_courses()

print(l[0].get_assignments()[0])
