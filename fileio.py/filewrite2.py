lst=["red","blue","green","yellow","white","cyan"]
path="C:\\Users\\LENOVO\\Desktop\\python\\fileio.py\\colors.txt"
fw=open(path,"w")
for c in lst:
    fw.write(c+"\n")