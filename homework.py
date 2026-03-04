# read a number and print number is +ve, -ve or zero 
num = int(input("enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


#read a single digit number and print its word form
n = int(input("enter a single digit number: "))
if n == 0:
    print("zero")
elif n == 1:
    print("one")
elif n == 2:
    print("two")
elif n == 3:
    print("three")
elif n == 4:
    print("four")
elif n == 5:
    print("five")
elif n == 6:
    print("six")
elif n == 7:
    print("seven")
elif n == 8:
    print("eight")
elif n == 9:
    print("nine")
else:
    print("Invalid Number")


#read a number and print number is prime or non-prime
num = int(input("enter a number: "))
if num <= 1:
    print("the number is not prime.")
else:
    for a in range(2, num):
        if num % a == 0:
            print("the number is not prime")
            break
    else:
        print ("the number is prime")   


#read a number and convert in reverse order
num = int(input("enter a number: "))
def revDigit(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev

print("reversed number: " , revDigit(num))


#read a number and print n fabonacci terms
num = int(input("enter a number: "))
a = 0
b = 1
for i in range(num):
    print(a, end = " ")
    c = a + b
    a = b
    b = c
  

          
  
  
  
