class Student:
    
    # Class variable
    college = "DBATU University"

    def __init__(self, name, age, course):
        # Instance variables
        self.name = name
        self.age = age
        self.course = course

    # Instance method
    def display_details(self):
        print("===== Student Details =====")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("College:", Student.college)

    # Instance method
    def study(self):
        print(self.name, "is studying", self.course)


student1 = Student("Jayshri", 19, "B.Tech AI/ML")
student2 = Student("Rahul", 20, "B.Tech CSE")

student1.display_details()
student1.study()

print()

student2.display_details()
student2.study()
