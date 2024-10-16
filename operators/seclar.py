num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if (num1<num2 and num1>num3) or (num1>num2 and num1<num3):
    print(f"{num1} is second largest")
#if num2>num3:
#   print("second largest:num2")
#else:
#   print("second lar:num3")
elif (num2>num1 and num2<num1) or (num2<num3 and num2>num1):
    print(f"{num2} is second largest")
#if num1>num3:
#   print("sec lar:num1")
#else:
#   print("sec lar:num3")
else:
    print(f"{num3} is  second largest")
#if num1>num2:
#   print("sec lar:num1")
#else:
#   print("sec lar:num2")