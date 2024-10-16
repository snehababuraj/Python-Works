yr=2024
if(yr%100==0 and yr%400!=0) or (yr%100!=0 and yr%4==0):
    print("leap year")
else:
    print("not leap year")

# i=1
# for i in range(0,10):
#     if i%2==0:
#         print(i)
#     i=i+1