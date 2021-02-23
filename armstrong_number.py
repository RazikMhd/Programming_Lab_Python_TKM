def armstrong_number(max):
    list = []
    counter = 1
    while(counter<=max):
        digit_cube_sum = 0
        counter_str = str(counter)
        for n in counter_str:
            n = int(n)
            digit_cube_sum = digit_cube_sum + (n*n*n)

        if(digit_cube_sum==counter):
            list.append(counter)
        counter = counter+1
    print("The armstrong numbers from 1 to 500 are : ")
    print(list)

armstrong_number(500)
