path="C:\\Users\\LENOVO\\Desktop\\python\\fileio.py\\colors.txt"
f=open(path,"r")
lst=[]
for line in f:
    lst.append(line.strip("\n"))
print(set(lst))