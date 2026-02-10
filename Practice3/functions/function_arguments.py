

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

def my_function(fname, lname):#multiple arguments
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#default parametr
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

def my_function(fruits): #list as argument, 
  for fruit in fruits:   #can be used different data
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)