students=[
    {"rol":100,"name":"arjun","course":"django"},
    {"rol":101,"name":"biju","course":"mearn"},
    {"rol":102,"name":"cijoy","course":"testing"},
    {"rol":103,"name":"vipin","course":"django"},
    {"rol":104,"name":"tom","course":"mearn"},
    {"rol":105,"name":"jhon","course":"testing"},
    {"rol":106,"name":"nibin","course":"django"},
]

#for dictionary in students:
#    print(dictionary.get("name"))

#for dictionary in students:
 #   print(dictionary.get("course"))

#print student name whose course= django value
for stud in students:
    if stud.get("course")=="django":
        print(stud.get("name")) 
    
