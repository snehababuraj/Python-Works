#vararg method :variable length argument method


#to read n numbers of arguments "*" is used.args recevie values as tuple

#def add_numbers(*agrs):
 #   print(agrs)
#add_numbers(10,20,30,30,40)
#add_numbers(10,20,30)


def add_numbers(*args):
    return sum(args)
#print(add_numbers(10,20))

#to recevie key word argument use (**kwargs) , take values as dictionary
#def display_student(**kwargs):
    #print(kwargs)
#display_student(id="400",name="vijay",total="550",course="msc")

#def display_mobile(**kwargs):
#    print(kwargs.get("name"))
#display_mobile(name="redminote10",price="35000",brand="redmi")

#text="longest word"
#words=text.split(" ")
def get_len(word):
    return(len(word))
#longest_word=max(words,key=get_len)
#print(longest_word)

#shortest_word=min(words,key=get_len)
#print(shortest_word)

def get_max_min(text,is_max=True):
    words=text.split(" ")
    if(is_max==True):
        longest_word=max(words,key=get_len)
        return longest_word
    else:
        shortest_word=min(words,key=get_len)
        return shortest_word
text="longest word"
print(get_max_min(text,is_max=False))
