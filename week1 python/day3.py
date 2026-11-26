#if-else, loops, functions are covered

#1 elif statement
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = weight/(height ** 2)
print("BMI =", round(bmi, 2))
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal Weight")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obesity I")
elif bmi < 40:
    print("Obesity II")
else:
    print("Obesity III")


#2 if-else break continue
numbers = [12, 5, -3, 8, 0, 15, 22, 7]
target = int(input("Enter number: "))
for num in numbers:

    if num < 0:
        continue    # Skip negative numbers

    if num == target:
        print("Number found:", num)
        break       # Stop searching

    print("Checking:", num)

else:
    print("Number not found")


#3 match statement
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator: ")

match operator:
    case "+":
        print("Result =", num1 + num2)

    case "-":
        print("Result =", num1 - num2)

    case "*":
        print("Result =", num1 * num2)

    case "/":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Division by zero is not allowed")

    case _:
        print("Invalid Operator")



#4 nested for loop
list1 = [1, 2, 3]
list2 = [3, 4, 5]
for i in list1:
    for j in list2:
        if i == j:
            print("Common Element:", i)


#5 while loop
n = int(input("Enter a number: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1

print("Sum =", total)


#6 functions largest number
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

result = largest(10, 25, 15)
print("Largest Number:", result)


#7 fibonacci series recursive
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter number of terms: "))

for i in range(terms):
    print(fibonacci(i), end=" ")