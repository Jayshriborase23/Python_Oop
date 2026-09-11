class Student:
    def display_details(self, name, age, course):
        print("===== Student Details =====")
        print("Name:", name)
        print("Age:", age)
        print("Course:", course)


student1 = Student()

student1.display_details(
    "Jayshri",
    19,
    "B.Tech AI/ML"
)
