from re import fullmatch
date="27-06-1804"
rule="((0[1-9]|[12]\d|3[01])[-]([1-9]|1[0-2])[-](18|19]\d{2}|20[01]\d|202[0-4]))"
matcher=fullmatch(rule,date)
print("invalid"if matcher==None else "valid")
