# text="zaheer"
# print(max(text))
# print(min(text))
# srt=sorted(text,reverse=True)
# print(srt)



# source_word="listen"
# target_word="silent"
# srt1=sorted(source_word)
# srt2=sorted(target_word)
# print(srt1)
# print(srt2)
# if srt1==srt2:
#     print("anagram")
# else:
#     print("not anagram")


source_word="chicken"
target_word="hen"
#kangaroo word

#q2
str1="abcd"
str2="pqrst"
#merge string
#out=apbqcrdst

# word=input("enter a string")
# length=len(word)-1
# srt=""
# for i in range(length,-1,-1):
#     srt=srt+word[i]
# print(srt)
# print ("palindrome" if srt==word else "not palindrome")

# text="this is a goodmorning msg"
# word=text.split(" ")
# def get_len(w):
#      return len(w)
# long=max(word,key=get_len)  #key=len #key is parameter 
# print("longest word is ",long)

# text="this is a goodmorning msg"
# word=text.split(" ")
# def get_len(w):
#      return len(w)
# long=min(word,key=get_len)   
# print("longest word is ",long)

text="this is a goodmorning msg"
word=text.split(" ")
def get_len(w):
     return len(w)
long=sorted(word,key=get_len,reverse=True)  #key=len #key is parameter 
print(long)
