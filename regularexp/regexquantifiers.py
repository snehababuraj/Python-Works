#quantifiers -*,+,?,{} to mention the quantity
from re import *
text="aabbaccaaaggabbaaaa*"
#pattern="a*" #chk any number of a including zero
#pattern="a{2}" #chk for 2a
#pattern="a{2,3}"  #chk min 2 max 3
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())