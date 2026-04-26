# Base Class (Encapsulation)
class Record:
    def __init__(self, record_id):
        self._record_id = record_id   # private variable

    def get_id(self):
        return self._record_id

    def set_id(self, new_id):
        self._record_id = new_id


# Derived Class (Inheritance)
class Course(Record):
    def __init__(self, course_id, name, credits, semester):
        super().__init__(course_id)
        self.name = name
        self.credits = credits
        self.semester = semester

    def display(self):
        print(f"Course ID: {self.get_id()}, Name: {self.name}, Credits: {self.credits}, Semester: {self.semester}")


# Derived Class
class Faculty(Record):
    def __init__(self, faculty_id, name):
        super().__init__(faculty_id)
        self.name = name
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

    def display(self):
        print(f"Faculty ID: {self.get_id()}, Name: {self.name}")
        print("Courses:", [c.name for c in self.courses])


# Main Program
def main():
    c1 = Course("CS101", "Python", 4, 3)
    f1 = Faculty("F001", "Dr.Rao")

    f1.assign_course(c1)

    print("\n--- COURSE DETAILS ---")
    c1.display()

    print("\n--- FACULTY DETAILS ---")
    f1.display()


if __name__ == "__main__":
    main()