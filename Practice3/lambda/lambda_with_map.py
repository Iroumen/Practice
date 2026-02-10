#map with lambda
nums=[1,2,3]
print(list(map(lambda x:x*2,nums)))

#map with multiple lists
a=[1,2,3]
b=[4,5,6]
print(list(map(lambda x,y:x+y,a,b)))

#map replacing function
def inc(x):return x+1
print(list(map(lambda x:inc(x),nums)))
