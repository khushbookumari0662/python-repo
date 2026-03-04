#list
numbers = [10, 20, 30, 40]
print("Original List:", numbers)

# get values
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# adding elements
numbers.append(50)          
numbers.insert(1, 15)       
print("After adding elements:", numbers)

# removing elements
numbers.remove(30)         
numbers.pop()               
print("After removing elements:", numbers)

# updating element
numbers[2] = 100
print("After updating:", numbers)

# extend() 
numbers.extend([60, 40])
print("after extend:", numbers)

# sort()
numbers.sort()
print("after sort:", numbers)

# reverse()
numbers.reverse()
print("After reverse:", numbers)

# index()
print("Index of 40:", numbers.index(40))

# del 
del numbers[2]
print("After deleting index 2:", numbers)

# length of list
print("Length of list:", len(numbers))

# loop
print("Elements in list:")
for n in numbers:
    print(n)

# list slicing
print("Sliced list (1:3):", numbers[1:3])

# checking element in list
if 20 in numbers:
    print("20 is present in the list")
else:
    print("20 is not present in the list")
