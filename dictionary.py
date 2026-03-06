#dictionary as keyword argument
def printValue(**kwargs):
    for key,value in kwargs.items():
        print(key, "=", value)

printValue(a=10, b=28, c="khushboo")
