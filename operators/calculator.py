num1=int(input("enter a number"))
num2=int(input("enter a number"))
op=input("enter operator")
if op=="+":
    result=num1+num2
    print(f"result {num1}+{num2}={result}")
elif op=="-":
    result=num1-num2
    print(f"result {num1}-{num2}={result}")
elif op=="/":
    result=num1/num2
    print(f"result {num1}/{num2}={result}")
elif op=="*":
    result=num1*num2
    print(f"result {num1}*{num2}={result}")
elif op=="%":
    result=num1%num2
    print(f"result {num1}%{num2}={result}")
else:
    print("enter valid operator")

