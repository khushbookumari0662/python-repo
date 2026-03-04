#tuple
t = (10, 20, 30, 40, 20)
print("Original Tuple:", t)

# Length of tuple
print("Length:", len(t))

#elements
print("First element:", t[0])
print("Last element:", t[-1])

# Slicing
print("Slice ", t[1:4])

# Count 
print("Count of 20:", t.count(20))

# Index 
print("Index of 30:", t.index(30))

# Concatenation 
t2 = (50, 60)
tuple = t + t2
print("After concatenation:", tuple)

# Loop through tuple
print("Elements in tuple:")
for i in t:
    print(i, end=" ")

