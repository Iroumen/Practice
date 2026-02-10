#basic key usage
nums=[5,1,9]
print(sorted(nums,key=lambda x:x))

#sorting complex objects
pairs=[(1,3),(2,1),(4,2)]
print(sorted(pairs,key=lambda x:x[1]))

#dynamic sorting rule
rev=True
print(sorted(nums,key=lambda x:-x if rev else x))
