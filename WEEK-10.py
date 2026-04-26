# WEEK 10 - Course Management System (Single File)

class Course:
    def __init__(self, code, name, credits, semester):
        self.code = code
        self.name = name
        self.credits = credits
        self.semester = semester

    def display(self):
        print(f"{self.code} | {self.name} | Credits: {self.credits} | Sem: {self.semester}")


class Faculty:
    def __init__(self, fid, name):
        self.fid = fid
        self.name = name
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

    def display(self):
        print(f"{self.fid} | {self.name}")
        print("Courses:", [c.name for c in self.courses])


# Storage
courses = []
faculties = []


# Functions
def add_course():
    code = input("Enter Course Code: ")
    name = input("Enter Course Name: ")
    credits = int(input("Enter Credits: "))
    semester = int(input("Enter Semester: "))

    c = Course(code, name, credits, semester)
    courses.append(c)
    print("✅ Course Added!\n")


def add_faculty():
    fid = input("Enter Faculty ID: ")
    name = input("Enter Faculty Name: ")

    f = Faculty(fid, name)
    faculties.append(f)
    print("✅ Faculty Added!\n")


def assign_course():
    fid = input("Enter Faculty ID: ")
    code = input("Enter Course Code: ")

    faculty = next((f for f in faculties if f.fid == fid), None)
    course = next((c for c in courses if c.code == code), None)

    if faculty and course:
        faculty.assign_course(course)
        print("✅ Course Assigned!\n")
    else:
        print("❌ Faculty or Course not found!\n")


def view_data():
    print("\n--- COURSES ---")
    for c in courses:
        c.display()

    print("\n--- FACULTY ---")
    for f in faculties:
        f.display()


# Main Menu
def main():
    while True:
        print("\n===== COURSE MANAGEMENT SYSTEM =====")
        print("1. Add Course")
        print("2. Add Faculty")
        print("3. Assign Course")
        print("4. View Data")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_course()
        elif choice == "2":
            add_faculty()
        elif choice == "3":
            assign_course()
        elif choice == "4":
            view_data()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()