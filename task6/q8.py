str="SnehaBABURAJ"
l=0
u=0
for t in str:
    if t.islower():
        l+=1
    else:
        u+=1
print("lowercase",l)
print("uppercase",u)