path="C:\\Users\\LENOVO\\Desktop\\python\\fileio.py\\worldcup.txt"
f=open(path,"r")
teams=[]
for line in f:
    remove_new_line=line.strip("\n").split(" ")
    teams.append(remove_new_line[1])
print(set(teams))
wc={t:teams.count(t) for t in set(teams)}
print(wc)
print(max([(v,k) for k,v in wc.items()]))