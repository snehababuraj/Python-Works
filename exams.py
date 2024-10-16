text="sneha"
wc={}
vowels="a","e","i","o","u"
v_count=0
for t in text:
    if t in vowels:
        v_count+=1
wc={t:text.count(t)for t in set(text)}
print(wc)