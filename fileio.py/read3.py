path="C:\\Users\\LENOVO\\Desktop\\python\\fileio.py\\story.txt"
f=open(path,"r")
all_words=[]
for line in f:
    remove_new_line=line.strip("\n")
    words=remove_new_line.split(" ")
    for w in words:
        all_words.append(w)
print(all_words)
wc={w:all_words.count(w) for w in set(all_words)}
print(wc)


