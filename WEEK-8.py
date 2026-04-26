import csv
import json

# Save Courses to CSV
def save_courses(courses, filename="courses.csv"):
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Credits", "Semester"])
            for c in courses:
                writer.writerow([c.get_id(), c.name, c.credits, c.semester])
    except Exception as e:
        print("Error saving courses:", e)


# Load Courses from CSV
def load_courses(filename="courses.csv"):
    courses = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                courses.append(row)
    except FileNotFoundError:
        print("File not found!")
    return courses


# Save Faculty to JSON
def save_faculty(faculty_list, filename="faculty.json"):
    try:
        data = []
        for f in faculty_list:
            data.append({
                "id": f.get_id(),
                "name": f.name,
                "courses": [c.name for c in f.courses]
            })
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print("Error saving faculty:", e)


# Load Faculty from JSON
def load_faculty(filename="faculty.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Faculty file not found!")
        return []