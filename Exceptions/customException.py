class evenError(Exception):
    pass
class nineError(Exception):
    pass

num = int(input("Enter a number : "))

try:
    if(num%2==0):
        raise evenError("Even numbers not allowed")
    elif(num==9):
        raise nineError("Number 9 not allowed")
    else:
        print(num)
except Exception as e:
    print(e)
