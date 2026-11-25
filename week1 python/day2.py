# today tuples, sets, dictionaries covered

#1 size of a tuple 
myTuple = ('includehelp', 'python', 3, 2021) 
tupleLength = len(myTuple)
print("Tuple : ", str(myTuple))
print("Tuple Length : ", tupleLength)


#2 a tuple to list 
myList = [9, 3, 1, 4]
print("Initially List : " + str(myList))
myTuple = (2, 6)
myList += myTuple
print("List after Addition : " + str(myList))


#3 adding items and updating sets
companies = {'Lacoste', 'uspolo'}
print('Initial Set:',companies)
companies.add('zara')
print('Updated Set:',companies) 
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)


#4 adding, deleting and updating dictionary
dict1 = {"name": "sathvk", "city": "Hyderabad","age":22}
dict1["country"]="India"
print("dict1 =", dict1)
dict1.pop("age")
print("dict1 =", dict1)
dict2 = {}
dict2.update(dict1)
dict1.clear()
print("dict1 =", dict1)
print("dict2 =", dict2)

#5 type casting
a = 7
print(type(a)) 
b = 3.0
print(type(b)) 
c = a + b 
print(c) 
print(type(c))
d = a * b
print(d)
print(type(d))

s = '7'
n = a + int(s)
print(n)        
print(type(n))