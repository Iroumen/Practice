class Animal:
    def sound(self):
        print("Some sound")  #Parent method

class Dog(Animal):
    def sound(self):
        print("Bark")  #Overrides parent method

Dog().sound()    #Bark
Animal().sound() #Some sound
