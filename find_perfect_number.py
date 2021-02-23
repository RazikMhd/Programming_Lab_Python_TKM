def p_number(number):
    factors = []
    counter = 1
    while(counter<number):
        if(number%counter==0):
            factors.append(counter)
        counter+=1
    if(sum(factors)==number):
        print(str(number)+" is a perfect number.")
    else:
        print(str(number) + " is a not perfect number.")

p_number(6)