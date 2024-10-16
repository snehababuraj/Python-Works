# #armstrong number
# num=153
# sum=0
# while(num!=0):
#     digit=num%10
#     cube=digit**3
#     sum=sum+cube
#     num=num//10
# print(sum)

num=153
digit_count=len(num) # function to find length of a string
num=int(num)
org=num
sum=0
while(num!=0):
    digit=num%10
    exp=digit**digit_count
    sum=sum+exp
    num=num//10
print(sum)
print("armstrong" if sum==org else "not armstrong")