from re import *
text="num1"
pattern="[a-zA-Z][a-zA-Z0-9_]*"
matcher=fullmatch(pattern,text)
if matcher==None:
    print("Invalid")
else:
    print("Valid")