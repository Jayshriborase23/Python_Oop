
class Student:
    def show_role(self):
        print("I am a student.")


class AIMLStudent(Student):
    def show_role(self):
        print("I am an AI/ML student.")


class CSEStudent(Student):
    def show_role(self):
        print("I am a CSE student.")


student1 = AIMLStudent()
student2 = CSEStudent()

student1.show_role()
student2.show_role()
