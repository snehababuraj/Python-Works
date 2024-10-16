from re import fullmatch
pan_card="DTZPS6463J9"
#first 3 alphabet
#4 th place P C A F H T
#5th alphanet
#followed by 4 digits
#alphabet in last place
rule="[A-Z]{3}[PCAFHT][A-Z][0-9]{4}[A-Z]"
matcher=fullmatch(rule,pan_card)
print("Invalid"if matcher==None else "Valid")