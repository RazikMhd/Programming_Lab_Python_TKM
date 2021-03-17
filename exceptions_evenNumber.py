
number = int(input("Please enter a number : "))

try:
    assert number%2 == 0
    print("You entered No. "+str(number))
except:
    raise Exception("Sorry, no odd numbers allowed")




