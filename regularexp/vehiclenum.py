from re import *
text="KL-01-BN-7099"
rule="(KL)[-]?[0-9]{2}[-]?[A-Z]{1,2}[-]?[0-9]{4}"  #? - for optional
matcher=fullmatch(rule,text)
print("invalid" if matcher==None else "valid")