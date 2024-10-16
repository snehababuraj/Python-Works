#dict={}
#define{key:value,key:value,...} stored as key value pair
#key is unique(duplicate key not allowed)
#modification is allowed

# student={"id":1234,"name":"hari","gender":"male","course":"django"}
# # print(student["name"])
# # print(student["id"])
# # print(student["gender"])

expenses={"jan":12000,"feb":14000,"mar":13000,"apr":15000}
# # print(expenses["mar"])

# student["place"]="kakkanad" #add element into dict
# print(student)

#methods
#keys() return all the keys in dict
# all_keys=expenses.keys()
# for k in expenses:
#     print(k)

# for k in expenses.keys():
#     print(k)

course={"name":"djgano","language":"python","duration":7,"fees":50000,"faculty":"shyam"}
for k in course.keys():
   print(k)

#values() return all the values in dict
# for v in course.values():
    # print(v)

# items() return key value pair
# for k,v in course.items():
#     print(k,v)

#get(key) get the value in key,return none if we enter invalid key
# print(course.get("name"))
# print(course.get("fees"))
# print(course.get("duration"))

#update() to update
# course.update({"fees":60000})
# print(course)
# course.update({"duration":8,"fees":80000})
# print(course)


#pop(key) to remove keys value pair
#course.pop("faculty")
#print(course)
print(expenses.get("feb"))