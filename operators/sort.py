num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if (num1<=num2 and num1<=num3 and num2<=num3):
    print("sorted numbers are:",num1,num2,num3)
elif (num2<=num3 and num2<=num1 and num1<=num3):  
    print("sorted numbers are:",num2,num1,num3)
elif (num3<=num1 and num3<=num2 and num1<=num2):
    print("sorted numbers are:",num3,num1,num2)
elif (num1<=num2 and num2<=num1 and num3<=num1):
    print("sorted numbers are:",num1,num3,num2)
elif (num2<=num3 and num2<=num1 and num3<=num1):
    print("sorted numbers are:",num2,num3,num1)
elif (num3<=num1 and num3<=num2 and num2<=num1):
    print("sorted numbers are:",num3,num2,num1)

