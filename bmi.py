weight=float(input("enter weight in kg:"))
height=float(input("enter height in meters"))
bmi=weight/(height**2)

if bmi<18.5:
    print("the bmi is underweight")
elif bmi<25:
    print("the bmi is normal")
elif bmi<30:
    print("overweight")
else:
    print("obese")
    print("bmi",bmi)
