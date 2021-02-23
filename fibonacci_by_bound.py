def getFibonacci(start,end):
    length = end

    series = [0,1]
    if(length == 1):
        print(str([0]))

    if(length == 2):
        print(str([0,1]))

    if(length>=3):
        i = 2
        while(i<length):
            term = series[i-2]+series[i-1]
            series.append(term)
            i=i+1

    filtered = list(filter(lambda x: (x >= start) and (x <= end), series))
    return filtered


