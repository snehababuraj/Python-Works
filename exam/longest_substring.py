text="acabcdaad"
palindrome_lst=[]
for i in range(len(text)):
    p=i
    n=i
    #odd position
    while(p>=0 and n<len(text) and text[p]==text[n]):
        palindrome_text=text[p:n+1]
        palindrome_lst.append(palindrome_text)
        n=n+1
        p=p-1
    p=i
    n-i+1
    #even position
    while(p>=0 and n<len(text) and text[p]==text[n]):
        palindrome_text=text[p:n+1]
        palindrome_lst.append(palindrome_text)
        p-=1
        n+=1
print(palindrome_lst)
def get_length(w):
    return len(w)
print(max(palindrome_lst,key=get_length))
