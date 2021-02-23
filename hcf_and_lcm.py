num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))

hcf = 1
lcm = 1

for div in range(1,num1):
    if((num1%div==0)and(num2%div==0)):
        hcf = div

lcm = int((num1*num2)/hcf)

print("HCF of "+str(num1)+" and "+str(num2)+" is "+str(hcf))
print("LCM of "+str(num1)+" and "+str(num2)+" is "+str(lcm))