# to define a list 
# []=list object 
#list()
# duplicates are allowed, insertion order is preserved, mutable

# languages=["python","js","java","python"]
# # print(languages)
# # print(languages[2])
# # print(languages[0])

# languages[1]="javascript"
# print(languages)


expenses=[15000,20000,16000,17000,25000]
#print(expenses)
# print(expenses[1])
#expenses[2]=18000
#print(expenses)

#for i in range(0,len(expenses)): #print values one by one
    #print(expenses[i])

#for obj in expenses:
    #print(obj)

# for obj in expenses:
#     if obj>19000:
#         print(obj)



# for obj in expenses:
#     # if(obj>=15000 and obj<=18000):
#     #     print(obj) 

# to print total expense
sum=0
for obj in expenses:
    sum=sum+obj
print(sum)

# sum=sum(expenses)
# print(sum)

# max=max(expenses)
# print(max)
# min=min(expenses)
# print(min)
#sort=sorted(expenses,reverse=True) #true=descinding order largest-smallest
#print(sort)

