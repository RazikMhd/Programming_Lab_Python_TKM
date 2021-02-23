import math

def get_squares(start,end):
    dict = {}
    squares = [i*i for i in range(int(math.sqrt(end)+1))]
    filtered = list(filter(lambda x: (x >= start)and(x <= end), squares))
    for i in filtered:
        dict[str(int(math.sqrt(i)))] = str(i)
    return dict
