
#The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break  #Exit the loop when x is "banana"
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break #Exit the loop when x is "banana"
  print(x) #But this time the break comes before the print



