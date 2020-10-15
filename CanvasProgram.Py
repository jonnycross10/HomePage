from canvasapi import Canvas
from secrets import url,apiKey
import json
from datetime import datetime

canvas = Canvas(url,apiKey)

usr = canvas.get_current_user()

l = usr.get_courses()

'''
the old way to print course/assignments
for i in range(0,3):
  print(l[i])
  for n in l[i].get_assignments():
    print(n,n.due_at, n.in_closed_grading_period,"\n")
'''


#I put the courses and assignments into a dictionary
d = {}
for i in range(0,4):
  d[l[i].name] = []
  for n in l[i].get_assignments():
    d[l[i].name].append(n.name)


#this shows the assignments i have sorted by due date
cs130 = l[0].get_assignments(order_by = "due_at")
ddate = cs130[0].due_at

#have to cut off trailing z to convert correctly
date = datetime.fromisoformat(ddate[0:19])
t = datetime.now()

upcoming_assignments = []

def isAssDue(assDate):
  if(assDate == None):
    return False
  if(datetime.fromisoformat(assDate[0:19])>t):
    return True
  return False


for i in range(0,4):
  course_ass = l[i].get_assignments(order_by = "due_at")
  for j in course_ass:
    if(isAssDue(j.due_at)):
      upcoming_assignments.append(j.name)

print(upcoming_assignments)

'''

with open('ass.js', 'w') as f:
  f.write("var cs130a = " +str(d[l[0].name]) +";\ndocument.getElementById('cs130a').innerHTML = cs130a;\n")

with open('ass.js', 'a') as f:
  f.write("var cs131a = " +str(d[l[1].name]) +";\ndocument.getElementById('cs131a').innerHTML = cs131a;\n")

with open('ass.js', 'a') as f:
  f.write("var phil103a = " +str(d[l[2].name]) +";\ndocument.getElementById('phil103a').innerHTML = phil103a;\n")

with open('ass.js', 'a') as f:
  f.write("var pubh50a = " +str(d[l[3].name]) +";\ndocument.getElementById('pubh50a').innerHTML = pubh50a;")

#Then put the dictionary into a json file
with open('assignments.json', 'w') as fp:
    json.dump(d, fp)
'''


'''
Okay so in canvas official documentation I can call the keys in the json response.
EX:
 "14": { "due_at": "2015-09-05", "grading_period_id": null, "in_closed_grading_period": false },
"15": { due_at: null, "grading_period_id": 3, "in_closed_grading_period": true }

valid : assignment.due_at, assignment.grading_period_id, assignment.in_closed_grading_period.
'''
