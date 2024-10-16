num=int(input("enter a number"))
def next_pal(num):
    while(True):
        if num!=0:
            org=num
        else:
            num=org
        result=""
        while(num!=0):
            digit=num%10
            result=result+str(digit)
            num=num//10
        if  int(result)==org:
            return(org)
        org=org+1
if num==next_pal(num):
    print(next_pal(num+1))
else:
    print(next_pal)




# next prime number

# num=int(input("enter number"))
# while(True):
#     if(num>=1):
#         for i in range(2,num):
#             if(num%2==0):
#                 break
