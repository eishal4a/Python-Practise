class Student:
    def putdata(self):
        self.id = input("Enter the student ID: ")
        self.name = input("Enter the student name: ")
        self.marks = float(input("Enter the student marks: "))  

    def display(self):
        print("Student ID:", self.id)
        print("Student Name:", self.name)
        print("Student Marks:", self.marks)


obj = Student()
obj.putdata()
obj.display()
