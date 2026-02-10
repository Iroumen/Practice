#filter
nums=[1,2,3,4]
print(list(filter(lambda x:x%2==0,nums)))

#filter using condition from function
def ok(x):return x>2
print(list(filter(lambda x:ok(x),nums)))

#filter with truthy values
vals=[0,"hi","",5,None]
print(list(filter(lambda x:x,vals)))
