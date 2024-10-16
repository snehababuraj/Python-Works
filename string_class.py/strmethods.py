# data1="this ia string"
# data2='this is also string'
# # to print more than one line """
# data3="""" 

#        this
#        is      
#        also
#        string
# """
# print(data3)
# print(data1)
# print(data2)

# # python consider these data as sting object.
# # class (blue print, plan, design pattern,template(these are the attributes of class))
# # class contain attributes and methods.
# # objects are real world entity. 

text="this is a goodmorning message"
#print longest word in the string
word=text.split(" ")
print(word)
def get_len(w):
    return len(w)
max_word=max(word,key=get_len)
print("longest word in the text is:",max_word)
min_word=min(word,key=get_len)
print("shortest word in the text is:",min_word)
srt_words=sorted(word,key=get_len,reverse=True)
print("sorted order",srt_words)