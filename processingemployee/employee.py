from json import load
f=open("C:\\Users\\LENOVO\\Desktop\\python\\processingemployee\\data.json","r")
employees=load(f)
#print(employees)

#q1 num of employees
#print(len(employees))

#q2 print all employee name
#for dict in employees:
 #   print(dict.get("name"))
employee_name=[e.get("name")for e in employees]
#print(employee_name)

#q3 print employee names working as qa
dept=[e.get("name")for e in employees if e.get("department")=="qa"]
#print(dept)

#q4 location ekm
loaction=[e.get("name")for e in employees if e.get("location")=="ekm"]
#print(loaction)

#q5