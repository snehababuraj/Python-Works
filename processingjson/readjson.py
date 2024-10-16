from json import load
f=open("C:\\Users\\LENOVO\\Desktop\\python\\processingjson\\student.json","r")
data=load(f)
#for dictionary in data:
    #print(dictionary.get("name"))
    #print(dictionary.get("place"))
    #if dictionary.get("place")=="thrissur":
     #   print(dictionary.get("name"))
#place=[dictionary.get("name")for dictionary in data if dictionary.get("place")=="thrissur"]
#print(place)

#all_course=[dictionary.get("course") for dictionary in data]
#print(set(all_course))

st=set()
for dictionary in data:
    course=dictionary.get("course")
    st.add(course)
print(st)

#to unpack to dictionary python use **

dictionary1={"one":1,"two":2,"three":3}

dictionary2={"four":4,"five":5,"six":6}
newdict={**dictionary1,**dictionary2}
print(newdict)