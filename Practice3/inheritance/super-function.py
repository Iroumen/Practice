class Animal:
    def __init__(self, name):
        self.name = name  #Parent instance variable

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)  #Call parent constructor

d = Dog("Max")
print(d.name)  #Access inherited variable
