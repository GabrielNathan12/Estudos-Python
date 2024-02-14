def recursiva(start=0, end=10):

    if start >= end:
        return end
    
    print(start, end)
    start += 1
    return recursiva(start, end)



print(recursiva())