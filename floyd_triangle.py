height = int(input("enter height of floyd triangle : "))

counter = 1
items = 1

for i in range(height):
    line = ""
    for j in range(items):
        line = line+str(counter)
        counter += 1
    print(line)
    items +=1


