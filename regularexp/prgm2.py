from re import *
text="fatboy@2k2#"
#pattern="\d" #match digits predefined characters
#pattern="\D" #exclude digits "[^0-9]"
#pattern="\w"  #for alphanumeric
#pattern="\W"   #for special characters
#pattern="\s"  for space
#pattern="\S"  for exclude space
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())