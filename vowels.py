text="Hello hello"
result=text.casefold()
print(result)
vowels=["a","e","i","o","u"]
count=0
for ch in result:
    if ch in vowels:
        count+=1
print(count)