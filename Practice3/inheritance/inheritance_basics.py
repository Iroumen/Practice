class Animal:
    def eat(self):
        print("Animal eats")  #Parent method

class Dog(Animal):
    def bark(self):
        print("Dog barks")  #Child-specific method

d = Dog()
d.eat()   #Inherited from Animal
d.bark()  #Defined in Dog
