from canvasapi import Canvas
from secrets import apiKey

canvas = Canvas(url,apiKey)

usr = canvas.get_current_user()

l = usr.get_courses()

headers = {"Authorization":"Bearer "+apiKey+"", "Content-Type": "json"
 }

r = requests.get("https://csus.instructure.com/api/v1/courses/64923/users/99221?include[]=enrollments", headers = headers)
print(r.text)
