from re import fullmatch
year="2019"
#1800-2024
rule="(18|19]\d{2}|20[01]\d|202[0-4])"
matcher=fullmatch(rule,year)
print("invalid"if matcher==None else "valid")