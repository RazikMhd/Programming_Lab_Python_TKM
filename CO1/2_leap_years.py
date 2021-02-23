import datetime
now = datetime.datetime.now()
currentyear = int(now.year)
targetyear = int(input("Please input an year : "))

list = []

while(currentyear<=targetyear):
    if(currentyear%100==0):
        if(currentyear%400==0):
            list.append(currentyear)
    else:
        if(currentyear%4==0):
            list.append(currentyear)

    currentyear=currentyear+1

print(list)


