number = 15
marks = 82

# Simple if
if number > 0:
    print("Number is positive")

# if-else
if number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# if-elif-else
if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 50:
    print("Grade B")
else:
    print("Fail")

# Nested if
if number > 0:
    if number % 5 == 0:
        print("Number is positive and divisible by 5")
