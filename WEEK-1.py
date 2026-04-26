course_code = input("Enter course code: ")
course_name = input("Enter course name: ")
credits = int(input("Enter credits: "))
semester = int(input("Enter semester: "))

if credits <= 0:
    print("Invalid credits")
else:
    print("\nCourse Details:")
    print(f"Code: {course_code}")
    print(f"Name: {course_name}")
    print(f"Credits: {credits}")
    print(f"Semester: {semester}")