tummy_size=int(input("enter tummy size"))
buttock_size=int(input("enter buttock size"))
gender=input("enter the gender")
values=tummy_size/buttock_size
values=round(values,2)
print(values)
# if (values<=0.80 and gender=="female") or (values<=0.95 and gender=="male"):
#     print("low")
# elif (values<=.85 and gender=="female") or (values<1.0 and gender=="male")::
#     print("moderate")
# elif (values>0.85 and gender=="female") or (values>=1.0 and gender=="male"):):
#     print("high")
if gender=="male":
    if values<=0.95:
        print("low health risk")
    elif values<1.0:
        print("moderate health risk")
    elif values>1.0:
        print("high health risk")
elif gender=="female":
    if values<=0.80:
        print("low health risk")
    elif values<=0.85:
        print("moderate health risk")
    elif values>0.85:
        print("high health risk")