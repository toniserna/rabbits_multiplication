# Rabbits multiplication algorithm
# The rabbits which were born 5 months ago they all die
# A variation on the Fibonacci's number calculation

def rabbits(n):
    list = [0, 0, 0, 0, 1]  
    for i in range(n-1):
        list.append(list[3] + list[4] - list.pop(0))

    return list[4]
