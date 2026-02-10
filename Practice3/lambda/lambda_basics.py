#Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

#lambda inside function
def myfunc(n):
  return lambda a : a * n

