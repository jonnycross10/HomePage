from canvasapi import Canvas
import requests
import json
apiKey = "*******************"
url = "*************"

canvas = Canvas(url,apiKey)

usr = canvas.get_current_user()

l = usr.get_courses(include = "total_scores")
e={}

for i in range(0,4):
  headers = {"Authorization":"Bearer "+apiKey+"", "Content-Type": "json"
  }

  r = requests.get("https://csus.instructure.com/api/v1/courses/"+str(l[i].id)+"/users/99221?include[]=enrollments", headers = headers)

  jsn = r.json()
  e[l[i].course_code] = jsn['enrollments'][0]['grades']['current_score']
  #print(l[0],jsn['enrollments'][0]['grades']['current_score'])
  #stu id 99221
  #course id 64923

  #https://csus.instructure.com/api/v1/courses/64923/users/99221?include[]=enrollments
print(e)

f1 = open("grades.js", "w")
f1.write("var cs130Grade = \""+ str(e[l[0].course_code])+ "\";\ndocument.getElementById('cs130').innerHTML = cs130Grade;\n")
f1.close()
f2 = open("grades.js", "a")
f2.write("var cs131Grade = \""+ str(e[l[1].course_code])+ "\";\ndocument.getElementById('cs131').innerHTML = cs131Grade;\n")
f2.close()

f3 = open("grades.js", "a")
f3.write("var phil103Grade = \""+ str(e[l[2].course_code])+ "\";\ndocument.getElementById('phil103').innerHTML = phil103Grade;\n")
f3.close()
f4 = open("grades.js", "a")
f4.write("var pubh50Grade = \""+ str(e[l[3].course_code])+ "\";\ndocument.getElementById('pubh50').innerHTML = pubh50Grade;\n")
f4.close()
