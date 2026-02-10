class Father:
    def skill(self):
        print("Coding")  #Father method

class Mother:
    def skill(self):
        print("Painting")  #Mother method

class Child(Father, Mother):
    pass

Child().skill()  #Coding, follows Method Resolution Order (Father first)
