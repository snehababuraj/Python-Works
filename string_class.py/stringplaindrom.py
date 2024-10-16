word="amam"
result=""
length=len(word)-1
for i in range(length,-1,-1):
    result=result+word[i]
print("plaindrome"if result==word else "not plaindrome")