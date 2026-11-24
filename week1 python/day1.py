#1 prime numbers
n = int(input("Enter a number: "))
c = 0
for i in range(2, (n // 2) + 1):
    if n % i == 0:
        c += 1
        break 
if c == 0 and n > 1:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")



#2 palindrome 
def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
s = input("Enter string: ")
if is_palindrome(s):
    print(s,"is a palindrome.")
else:
    print(s,"is not a palindrome.")



#3 list join
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)



#4 list comprehension  
names = ["mahi", "anu", "charan", "vivek", "sathvik"]
newlist = [x for x in names if "a" in x]
print(newlist)
 
