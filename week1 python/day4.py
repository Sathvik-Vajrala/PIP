#1 writing lists as arrays
arr = [10, 20, 30, 40, 50]
arr.sort()
print("Second Largest:", arr[-2])

#2 lambda function
square = lambda x: x * x
print(square(5))

#3 filter function
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#4 decorators
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def greet():
    print("Hello!")

greet()
