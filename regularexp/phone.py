from re import *
phone_num="+919656198197"
rule="(\+91)?[0-9]{10}"   #+ or . use \
matcher=fullmatch(rule,phone_num)
print("Invalid" if matcher==None else "valid")