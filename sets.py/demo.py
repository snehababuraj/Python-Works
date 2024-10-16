# st={vales}
# st=set() #to create an empty set

# insertion order is not preserved
# indexing is not supported in set
# duplicates are not allowed
# mutable

# st={10,20,10,30,"hello",True}
# print(st)
#methods

#add()
# st={10,20,40,30}
# st.add(50)
# print(st)

# #pop()
# st.pop() #remove random element from set
# print(st)

# remove(values) remove specific values, if value is not prsent it will return kry error
# st.remove(40)
# print(st)

# discard()
# st.discard(400) #remove elements not present in set return none
# print(st)

#union()
st1={10,20,30,40}
st2={30,40,50,60}
# union_set=st1.union(st2)
# print(union_set)

#intersection() #common in st1 and st2
# inter_set=st1.intersection(st2)
# print(inter_set)

#difference()
dif_set=st1.difference(st2) #present in st1 not in st2, st1 nn st2 ile elemnts remove chyummm
print(dif_set)

#copy()
#update()

colors={"red","green","blue"}
new_colors={"cyan","purple","brown"}
colors.update(new_colors)
print(colors)