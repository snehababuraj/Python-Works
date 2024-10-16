from re import fullmatch
date="18"
rule="(0[1-9]|[12][0-9]|3[01])"
matcher=fullmatch(rule,date)
print("Invalid"if matcher==None else "Valid")