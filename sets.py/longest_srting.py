# lst=[10,20,20,50,40,20]
# st=set(lst)
# # print(st)
#dhoni suggestion
all_users={"sachin","darvid","laxman","jadeja","dhoni","raina"}
dhoni_frnds={"sachin","raina"}
dif_set=all_users.difference(dhoni_frnds)
dif_set.discard("dhoni")
print(dif_set)

