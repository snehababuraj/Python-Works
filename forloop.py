# range(start,stop,step=1)
# print("msg",end="\n"default value) to print in one line end=""
# \n=newline

# num=int(input("enter number"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)

for i in range(1,5):
    print(i, end="\t")
for i in range(1,5):
    print("*",end="\t")
print()
for i in range(1,5):
    print("*", end="$")
print("\nline end")

for i in range(1,11):
    print(i,end="@")
print("\nline end")

for row in range(1,5):
    for col in range(1,4):
        print(col,end="\t")
    print("\n")

