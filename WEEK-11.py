# WEEK 11 - Timetable Scheduling System

class Course:
    def __init__(self, code, name):
        self.code = code
        self.name = name


class Faculty:
    def __init__(self, fid, name):
        self.fid = fid
        self.name = name


class Timetable:
    def __init__(self):
        self.schedule = {}   # {(day, time): (course, faculty)}

    def add_class(self, day, time, course, faculty):
        key = (day, time)

        # Check time slot conflict
        if key in self.schedule:
            print("❌ Time slot already booked!")
            return

        # Check faculty conflict
        for (d, t), (c, f) in self.schedule.items():
            if d == day and t == time and f.fid == faculty.fid:
                print("❌ Faculty already assigned at this time!")
                return

        self.schedule[key] = (course, faculty)
        print("✅ Class added successfully!")

    def display(self):
        if not self.schedule:
            print("No classes scheduled.")
            return

        print("\n--- TIMETABLE ---")
        for (day, time), (course, faculty) in self.schedule.items():
            print(f"{day} {time} - {course.name} ({faculty.name})")


# Storage
courses = []
faculties = []
tt = Timetable()


# Functions
def add_course():
    code = input("Enter Course Code: ")
    name = input("Enter Course Name: ")
    courses.append(Course(code, name))
    print("✅ Course Added!")


def add_faculty():
    fid = input("Enter Faculty ID: ")
    name = input("Enter Faculty Name: ")
    faculties.append(Faculty(fid, name))
    print("✅ Faculty Added!")


def schedule_class():
    day = input("Enter Day: ")
    time = input("Enter Time: ")
    code = input("Enter Course Code: ")
    fid = input("Enter Faculty ID: ")

    course = next((c for c in courses if c.code == code), None)
    faculty = next((f for f in faculties if f.fid == fid), None)

    if course and faculty:
        tt.add_class(day, time, course, faculty)
    else:
        print("❌ Course or Faculty not found!")


def view_timetable():
    tt.display()


# Menu
def main():
    while True:
        print("\n===== TIMETABLE SYSTEM =====")
        print("1. Add Course")
        print("2. Add Faculty")
        print("3. Schedule Class")
        print("4. View Timetable")
        print("5. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            add_course()
        elif ch == "2":
            add_faculty()
        elif ch == "3":
            schedule_class()
        elif ch == "4":
            view_timetable()
        elif ch == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()