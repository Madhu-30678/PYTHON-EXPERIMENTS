courses = []

while True:
    print("\n1. Add Course")
    print("2. View Courses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        code = input("Enter course code: ")
        courses.append(code)

    elif choice == "2":
        print("Courses:", courses)

    elif choice == "3":
        break