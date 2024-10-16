# prev=0
# current=1
# print(prev)
# print(current)
# for i in range(0,10):
#     next=prev+current
#     print(next)
#     prev=current
#     current=next
    

# prev=0
# current=1
# print(prev)
# print(current)
# limit=100
# next=1
# while(next<=limit):
#     print(next)
#     prev=current
#     current=next
#     next=prev+current



num=21
is_fibo=False
prev=0
current=1
next=prev+current
while(next<=num):
    if next==num:
        is_fibo=True
        break
    prev=current
    current=next
    next=prev+current
print(is_fibo)




