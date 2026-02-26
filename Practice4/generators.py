#Create a generator that generates the squares of numbers up to some number N
def square(n):
    for i in range(n + 1):
        yield i * i

n = int(input())
for value in square(n):
    print(value)


#Generator to print even numbers between 0 and n (comma-separated)
def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
print(",".join(str(x) for x in even_numbers(n)))


#Generator for numbers divisible by both 3 and 4 between 0 and n
def div_12(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for num in div_12(n):
    print(num)

#Generator squares(a, b) → squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i
for value in squares(2, 6):
    print(value)

#Generator that returns numbers from n down to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for num in countdown(n):
    print(num)