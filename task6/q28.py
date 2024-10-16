 
def find_max(a, b, c):
    if (a >= b) and (a >= c): 
        return a
    elif (b >= a) and (b >= c): 
        return b
    else:
        return c
print("maximum of three number :-" ,find_max(10,2,30))