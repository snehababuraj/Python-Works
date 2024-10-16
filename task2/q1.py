num1=45
num2=35
largest_num=max(num1,num2)
while(True):
   if largest_num%num1==0 and largest_num%num2==0:
      lcm=largest_num
      break
   largest_num=largest_num+1
print(lcm)
