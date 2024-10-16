def unique_string(text):
    common_chars=[]
    for ch in text:
        if ch not in common_chars:
            common_chars.append(ch)
    return("").join(common_chars)  #join - to append the word from common_chars
print(unique_string("helloworld"))


#longest_sub string