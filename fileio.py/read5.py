path="C:\\Users\\LENOVO\\Desktop\\python\\fileio.py\\orders.txt"
f=open(path,"r")
items=[]
for line in f:
    data=line.strip("\n")
    items.append(data)
print(set(items))
wc={i:items.count(i) for i in set(items)}
print(wc)
print(max([(v,k) for k,v in wc.items()]))
print(min([(v,k) for k,v in wc.items()]))
print(sorted([(v,k) for k,v in wc.items()],reverse=True))