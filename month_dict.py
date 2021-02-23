months = {"january":31,"february":28,"march":31,"april":30,"may":31,"june":30,"july":31,"august":31,"september":30,"october":31,"november":30,"december":31}

user_input = input("please enter a month name in lower-case : ")
try:
    print(months[user_input])
except:
    print("Given month doesn to exist")

sorted_keys = list(months.keys())
sorted_keys.sort()
print("Sorted month list : ")
print(sorted_keys)


list_30 = list(filter(lambda x: (months[x]==30),[x for x in sorted_keys]))
print("months with 30 days : ")
print(list_30)

# for name in sorted_keys:
#     if(months[name]) == 30:
#         list_30.append(sorted_keys)