height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = (weight / height / height ) * 10000

print(f"Your BMI is {BMI}")

if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severly obese.")