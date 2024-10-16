l1=[10,13,20,30,32,15]
l2=[15,16,20,30,31]
result=[]
for num in l1:
    if num in l2:
        result.append(num)
print(result)