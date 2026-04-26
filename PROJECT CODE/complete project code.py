# ==========================================
# COURSE TIMETABLE & COURSE MANAGEMENT SYSTEM
# ==========================================

import csv
import json

# Safe import for matplotlib
try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except:
    MATPLOTLIB_AVAILABLE = False

# ==========================================
# MODELS
# ==========================================

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

    def assign_course(self, course_code):
        if course_code not in self.courses:
            self.courses.append(course_code)

    def display(self):
        print(f"{self.fid} | {self.name} | Courses: {self.courses}")


# ==========================================
# GLOBAL STORAGE
# ==========================================

courses = []
faculty_list = []
timetable = {}
course_codes = set()

# ==========================================
# VALIDATION
# ==========================================

def validate_course_code(code):
    return code.isalnum()

def validate_credits(credits):
    return credits > 0

# ==========================================
# COURSE FUNCTIONS
# ==========================================

def add_course():
    code = input("Enter Course Code: ").upper()

    if not validate_course_code(code):
        print("Invalid course code!")
        return

    if code in course_codes:
        print("Course already exists!")
        return

    name = input("Enter Course Name: ")
    credits = int(input("Enter Credits: "))

    if not validate_credits(credits):
        print("Invalid credits!")
        return

    semester = int(input("Enter Semester: "))

    c = Course(code, name, credits, semester)
    courses.append(c)
    course_codes.add(code)

    print("Course added successfully!")

def view_courses():
    if not courses:
        print("No courses available.")
        return

    for c in courses:
        c.display()

# ==========================================
# FACULTY FUNCTIONS
# ==========================================

def add_faculty():
    fid = input("Enter Faculty ID: ")
    name = input("Enter Faculty Name: ")

    f = Faculty(fid, name)
    faculty_list.append(f)

    print("Faculty added successfully!")

def assign_course_to_faculty():
    fid = input("Enter Faculty ID: ")
    course = input("Enter Course Code: ").upper()

    for f in faculty_list:
        if f.fid == fid:
            f.assign_course(course)
            print("Course assigned!")
            return

    print("Faculty not found!")

def view_faculty():
    if not faculty_list:
        print("No faculty available.")
        return

    for f in faculty_list:
        f.display()

# ==========================================
# TIMETABLE FUNCTIONS
# ==========================================

def add_timetable():
    day = input("Enter Day: ").capitalize()
    time = input("Enter Time Slot: ")
    course = input("Enter Course Code: ").upper()
    faculty = input("Enter Faculty ID: ")

    if day not in timetable:
        timetable[day] = []

    # Conflict detection
    for t in timetable[day]:
        if t[0] == time:
            print("Conflict! Time slot already booked.")
            return

    timetable[day].append((time, course, faculty))
    print("Timetable added successfully!")

def view_timetable():
    if not timetable:
        print("No timetable available.")
        return

    for day, slots in timetable.items():
        print("\n", day)
        for s in slots:
            print(f"Time: {s[0]} | Course: {s[1]} | Faculty: {s[2]}")

# ==========================================
# FILE HANDLING
# ==========================================

def save_courses():
    with open("courses.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for c in courses:
            writer.writerow([c.code, c.name, c.credits, c.semester])

def save_faculty():
    data = []
    for f in faculty_list:
        data.append({
            "id": f.fid,
            "name": f.name,
            "courses": f.courses
        })

    with open("faculty.json", "w") as file:
        json.dump(data, file)

# ==========================================
# ANALYTICS
# ==========================================

def faculty_workload_chart():
    if not MATPLOTLIB_AVAILABLE:
        print("Matplotlib not installed. Cannot show chart.")
        return

    names = []
    counts = []

    for f in faculty_list:
        names.append(f.name)
        counts.append(len(f.courses))

    if not names:
        print("No data for analytics.")
        return

    plt.bar(names, counts)
    plt.title("Faculty Workload")
    plt.xlabel("Faculty")
    plt.ylabel("Courses Assigned")
    plt.show()

# ==========================================
# MAIN MENU
# ==========================================

def main():
    while True:
        print("\n===== CTCMS MENU =====")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Add Faculty")
        print("4. Assign Course to Faculty")
        print("5. View Faculty")
        print("6. Add Timetable")
        print("7. View Timetable")
        print("8. Show Analytics")
        print("9. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_course()
        elif choice == "2":
            view_courses()
        elif choice == "3":
            add_faculty()
        elif choice == "4":
            assign_course_to_faculty()
        elif choice == "5":
            view_faculty()
        elif choice == "6":
            add_timetable()
        elif choice == "7":
            view_timetable()
        elif choice == "8":
            faculty_workload_chart()
        elif choice == "9":
            save_courses()
            save_faculty()
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice!")

# ==========================================
# START PROGRAM
# ==========================================

if __name__ == "__main__":
    main()