#with argument with return
def sum(a,b):
    c = a + b
    return c
#calling sum
r = sum(76, 67)
print(r)


#without argument with return
def sum():
    a = int(input())
    b = int(input())
    c = a + b
    return c
r = sum()
print(r)


#with argument no return
def sum(a,b):
    c = a + b
    print(c)
sum(54, 78)


#without argument no return
def sum():
    a = int(input())
    b = int(input())
    c = a + b
    print(c)
sum()  
