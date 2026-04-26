courses = []

courses.append(["CS101", "Python", 4])

search = input("Enter course code to search: ")

found = False
for c in courses:
    if c[0].lower() == search.lower():
        print("Found:", c)
        found = True

if not found:
    print("Course not found")