for row in range(1,6):
    for space in range(1,(6-row)):
        print(" ",end="")
    for col in range(1,row+1):
        print("* ",end="")
    print()

#next palindromic number
# num=606