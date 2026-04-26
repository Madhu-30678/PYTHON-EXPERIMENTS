class Timetable:
    def __init__(self):
        self.schedule = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": []
        }

    def add_class(self, day, time, course, faculty):
        # Conflict detection
        for entry in self.schedule[day]:
            if entry["time"] == time:
                if entry["faculty"] == faculty:
                    print("Conflict: Faculty already assigned!")
                    return
                if entry["course"] == course:
                    print("Conflict: Course already scheduled!")
                    return

        self.schedule[day].append({
            "time": time,
            "course": course,
            "faculty": faculty
        })
        print("Class added successfully!")

    def display(self):
        for day, classes in self.schedule.items():
            print(f"\n{day}")
            for c in classes:
                print(f"{c['time']} - {c['course']} ({c['faculty']})")