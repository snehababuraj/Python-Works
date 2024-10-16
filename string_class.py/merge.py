# str1="ABC"
# str2="PQR"
# len=len(str1)
# out=""
# for i in range(0,len):
#     out+=str1[i]+str2[i]
# print(out)
    


str1="ABCDEFGH"
str2="PQRST"
len=len(str2)
out=""
for i in range(0,len):
    out+=str1[i]+str2[i]
rem=str1[len:]
out+=rem
print(out)



# str1=input("enter string")
# str2=input("enter string")
# s1_len=len(str1)
# s2_len=len(str2)
# smallest_len=s1_len if s1_len<s2_len else s2_len
# out=""
# for i in range(0,smallest_len):
#     out+=str1[i]+str2[i]
# if len(str1)>len(str2):
#     rem=str1[smallest_len:]
# else:
#     rem=str2[smallest_len]
# out+=rem
# print(out)