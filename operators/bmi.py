# calculate bmi
# BMI(body mass index)

height_in_cm=int(input("enter height"))
weight_in_kg=int(input("enter weight"))
height_in_m=height_in_cm/100
bmi=weight_in_kg/(height_in_m**2)
print(bmi)
