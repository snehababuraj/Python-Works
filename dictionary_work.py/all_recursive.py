text="goodmorning"
# st_text=set(text)
# wc={}
# for ch in st_text:
#     wc[ch]=text.count(ch)
# print(wc)

wc={ch:text.count(ch) for ch in set(text)}
print(wc)
# wc={}
# for ch in text:
#     if ch in wc:
#         wc[ch]+=1
#     else:
#         wc[ch]=1
# for k,v in wc.items():
#     if v>1:
#         print(k)

