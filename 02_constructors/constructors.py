
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print("===== Student Details =====")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


student1 = Student("Jayshri", 19, "B.Tech AI/ML")
student2 = Student("Rahul", 20, "B.Tech CSE")

student1.display_details()

print()

student2.display_details()
