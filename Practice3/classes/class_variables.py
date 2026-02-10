
class Student:
    # Class variable
    school_name = "KBTU"

    def __init__(self, name, course):
        self.name = name  # Instance variable
        self.course = course  # Instance variable

    def show_info(self):
        # Accessing class variable inside method
        print(f"{self.name} studies at {Student.school_name} and is in course {self.course}")


# Creating instances
s1 = Student("Ayan", 10)
s2 = Student("Dinara", 11)

s1.show_info()
s2.show_info()

# Access class variable directly from class
print(Student.school_name)

# Change class variable
Student.school_name = "MIT"

s1.show_info()
s2.show_info()
