courses = []
course_codes = set()

code = input("Enter code: ")

if code in course_codes:
    print("Duplicate code!")
else:
    name = input("Enter name: ")
    course = {
        "code": code,
        "name": name,
        "credits": 4
    }
    courses.append(course)
    course_codes.add(code)

print(courses)