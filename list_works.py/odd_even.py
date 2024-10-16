numbers=[3,4,5,8,9,10]
odd=[]
even=[]
for num in numbers:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd)
