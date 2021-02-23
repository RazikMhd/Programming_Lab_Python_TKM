def getIntersection(array1,array2):
    intersection = [value for value in array1 if value in array2]
    return intersection

list1 = [1,2,3,4,5,6,7]
list2 = [2,4,6,8,10]

print(getIntersection(list1,list2))