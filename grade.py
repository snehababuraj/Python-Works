mark=int(input("Enter the Mark"))
total=int(input("Enter Total"))
percentage=(mark/total)*100
if percentage>=90:
    print("Grade A")
elif percentage>=80:
    print("Grade B")
elif percentage >=70:
    print("Grade C")
elif percentage<70:
    print("Fail")