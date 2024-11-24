weight  = float(input("enter weight in pound :"))
height = float(input("enter height in inches :"))

kg = weight*0.45359237
meter = height*0.0254
BMI = kg/(meter*meter)
print("BMI = ",BMI)