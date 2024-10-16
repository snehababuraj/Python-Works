text="ccaacbb"
wc={}
for ch in text:
    if ch in wc:
        print(ch,"is the first recursive character")
        break
    else:
        wc[ch]=1
