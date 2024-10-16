height_in_cm=int(input("enter your height"))
weight_in_kg=int(input("enter your weight"))
height_in_m=height_in_cm/100
bmi=weight_in_kg//(height_in_m**2)
print(bmi)
if bmi<18:
    print("underweight")
elif bmi<25:
    print("healthy")
elif bmi<30:
    print("Over weight")
elif bmi<35:
    print("Obese")
elif bmi>=35:
    print("Severe obesity")
