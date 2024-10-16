from re import *
text="abc K4gh$ 8fg"
#pattern="[a-z]"   #[]check for all lowercase alphabets -character sets
#pattern="[A-Z]"  #check for all uppercase alphabets
#pattern="[a-zA-Z]" #check all alphabets
#pattern="[0-9]"     #check for all digits
#pattern="[a-zA-Z0-9]"  #check alphanumeric characters
#pattern="[^a-zA-Z0-9]"   #exclude a-z,A-K,0-9
#pattern="[abc]"  check either a,b,c
matcher=finditer(pattern,text)
count=0
for m in matcher:
    print(m.start(),m.group())
    count+=1
print("number of alphabets",count)


#predefined character set
#quantifires