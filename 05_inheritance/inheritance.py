
class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class AIMLStudent(Student):
    
    def display_course(self):
        print("Course: B.Tech Artificial Intelligence & Machine Learning")


student = AIMLStudent("Jayshri", 19)

student.display_details()
student.display_course()
