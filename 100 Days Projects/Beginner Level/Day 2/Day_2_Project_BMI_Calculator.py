print("Tell the Height:\n")
height = input()

print("Tell the Weight\n")
weight = input()

height_float = float(height)

weight_int = int(weight)

cal = weight_int / height_float ** 2


bmi = int(cal)

print(bmi)