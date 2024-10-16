string="a2b4c6"
# print("orginal string :- " ,string)
alpha=[]
digit=[]
for t in string:
    if t.isalpha():
        alpha.append(t)
    else:
        digit.append(t)
result="".join(alpha+digit)
print(result)