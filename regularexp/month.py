from re import fullmatch
mnth="03"
rule="0[1-9]|1[0-2]"
matcher=fullmatch(rule,mnth)
print("invalid"if matcher==None else "valid")