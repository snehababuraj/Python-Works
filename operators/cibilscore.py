cibil_score=int(input("enter the cibil score"))
if cibil_score<550:
    print("Poor")
elif cibil_score<650: # cibil_score>= 550 and cibil_score<650
    print("Average")
elif cibil_score<750: # cibil_score>=650 and cibil_score<750
    print("Good")
elif cibil_score>=750:
    print("Excellent")