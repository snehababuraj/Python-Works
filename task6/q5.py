def is_diasirum(num):
    temp=0
    for i in range(len(str(num))):
        temp+=int(str(num)[i])**(i+1)
    return temp==num
num=int(input("enter number"))
print(is_diasirum(num))