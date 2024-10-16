text="pneumonoultramicroscopicsilicovolcanoconiosis"
vowels=("a","e","i","o","u")
v_count=0
c_count=0

# for ch in text:     to avoid space and spcl characters
#     if ch.isalpha():
#         char_couunt+=1
for ch in text:
    if ch in vowels:
        v_count=v_count+1
    else:
        c_count=c_count+1
print("v_count",v_count)
print("c_count",c_count)

#in is a membership operator