number = int(input("Enter a Number : "))

try:
    if(number%2 != 0):
        raise Exception("Odd Numbers not allowed ! ")
    else:
        print("You entered an even number !")
except Exception as e:
    print(e)

