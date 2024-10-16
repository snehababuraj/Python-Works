# i=1800
# while(i<=2024):
#     print(i)
#     i+=1

# i=1800
# while(i<=2024):
#     if i%100==0:
#         print(i)
#     i+=1

# i=1800
# while(i<=2024):
#     if i%100!=0:
#         print(i)
#     i+=1

i=1800
while(i<=2024):
    if (i%100==0 and i%400==0) or (i%100!=0 and i%4==0):
        print(i)
    i+=1
