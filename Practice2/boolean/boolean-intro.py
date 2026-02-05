print(10 > 9) #gives True
print(10 == 9) #gives value False
print(10 < 9) #also False

print(bool("Hello")) #here there is value so it is True
print(bool(15)) #same case

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#if there is any value, except int(0), str(""), etc. there will always True

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) #examples of bool value False

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

