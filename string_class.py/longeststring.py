text="goodmorning all"
word=text.split(" ")
def get_len(word):
    return len(word)
long=max(word,key=get_len)
print(long)