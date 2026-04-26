# WEEK 12 - File Handling (CSV & JSON)

import csv
import json

# Data storage
courses = []


# Functions
def add_course():
    code = input("Enter Course Code: ")
    name = input("Enter Course Name: ")
    credits = input("Enter Credits: ")
    semester = input("Enter Semester: ")

    course = {
        "code": code,
        "name": name,
        "credits": credits,
        "semester": semester
    }

    courses.append(course)
    print("✅ Course Added!")


def view_courses():
    if not courses:
        print("No courses available.")
        return

    print("\n--- COURSES ---")
    for c in courses:
        print(c["code"], "|", c["name"], "| Credits:", c["credits"], "| Sem:", c["semester"])


# SAVE TO CSV
def save_csv():
    with open("../PROJECT CODE/courses.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Code", "Name", "Credits", "Semester"])

        for c in courses:
            writer.writerow([c["code"], c["name"], c["credits"], c["semester"]])

    print("✅ Data saved to courses.csv")


# SAVE TO JSON
def save_json():
    with open("../PROJECT CODE/courses.json", "w") as f:
        json.dump(courses, f, indent=4)

    print("✅ Data saved to courses.json")


# LOAD FROM CSV
def load_csv():
    try:
        with open("../PROJECT CODE/courses.csv", "r") as f:
            reader = csv.DictReader(f)
            courses.clear()

            for row in reader:
                courses.append(row)

        print("✅ Data loaded from CSV")
    except FileNotFoundError:
        print("❌ CSV file not found!")


# LOAD FROM JSON
def load_json():
    try:
        with open("../PROJECT CODE/courses.json", "r") as f:
            data = json.load(f)
            courses.clear()
            courses.extend(data)

        print("✅ Data loaded from JSON")
    except FileNotFoundError:
        print("❌ JSON file not found!")


# MENU
def main():
    while True:
        print("\n===== FILE HANDLING SYSTEM =====")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Save to CSV")
        print("4. Save to JSON")
        print("5. Load from CSV")
        print("6. Load from JSON")
        print("7. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            add_course()
        elif ch == "2":
            view_courses()
        elif ch == "3":
            save_csv()
        elif ch == "4":
            save_json()
        elif ch == "5":
            load_csv()
        elif ch == "6":
            load_json()
        elif ch == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()