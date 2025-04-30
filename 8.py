
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")


student1 = Student("Ali", 101)
student1.display_info()
