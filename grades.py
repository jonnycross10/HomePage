from canvasapi import Canvas

canvas = Canvas(url,apiKey)

usr = canvas.get_current_user()

l = usr.get_courses(include = "total_scores")

#e = usr.get_enrollments(include[ "current_points"])
print(canvas.get_department_level_grade_data_current)
