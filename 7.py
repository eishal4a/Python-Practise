class Student:
    def putdata(self):
        self.id = input("Enter the student ID: ")
        self.name = input("Enter the student name: ")
        self.marks = float(input("Enter the student marks: "))  

    def display(self):
        print("\n\tStudent ID:", self.id)
        print("\tStudent Name:", self.name)
        print("\tStudent Marks:", self.marks)


obj = Student()
obj1 = Student()
obj.putdata()
obj1.putdata()
obj.display()
obj1.display()
