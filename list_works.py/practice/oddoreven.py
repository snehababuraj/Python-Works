numbers=[1,2,3,4,5,6,7,8]
even_lst=[]
odd_lst=[]
for num in numbers:
    if num%2==0:
        even_lst.append(num)

    else:
        odd_lst.append(num)

print(even_lst)
print(odd_lst)