list = []

counter = 32
end = 99

while(counter<=end):
    list.append(counter*counter)
    counter=counter+2

l_limit = int(input("Enter the starting of the range : "))
u_limit = int(input("Enter the ending of the range : "))

new_list = []

for num in list:
    if((num>l_limit)&(num<u_limit)):
        new_list.append(num)

print(new_list)


