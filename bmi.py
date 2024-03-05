# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

new_hight =float(height)
new_weight = int(weight)

bmi = new_weight / (new_hight**2)
# Write your code below this line 👇
print(int(bmi))