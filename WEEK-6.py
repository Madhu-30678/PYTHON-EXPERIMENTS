class Course:
    def __init__(self, code, name, credits):
        self.code = code
        self.name = name
        self.credits = credits

    def display(self):
        print(f"{self.code} - {self.name} ({self.credits} credits)")

c1 = Course("CS101", "Python", 4)
c2 = Course("CS102", "DSA", 3)

c1.display()
c2.display()