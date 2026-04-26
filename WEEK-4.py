courses = []

def add_course():
    code = input("Code: ")
    name = input("Name: ")
    courses.append([code, name])

def view_courses():
    for c in courses:
        print(c)

def search_course():
    code = input("Enter code: ")
    for c in courses:
        if c[0] == code:
            print("Found:", c)

add_course()
view_courses()
search_course()