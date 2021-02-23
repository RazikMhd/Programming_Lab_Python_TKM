odd_num = int(input("Enter an odd number greater than 1 : "))

def find_factorial(number):
    factorial = 1
    for i in range(number):
        factorial = factorial*(i+1)
    return factorial

def factorial_division(number):
    result = number/find_factorial(number)
    return result

counter = 1
sum = 0
while(counter<=odd_num):
    sum=sum+factorial_division(counter)
    counter=counter+2

print(sum)