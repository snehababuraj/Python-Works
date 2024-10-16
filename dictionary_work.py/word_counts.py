text="fat cat mat cat cat fat"
word=text.split(" ")
wc={}
for w in word:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1
print(wc)