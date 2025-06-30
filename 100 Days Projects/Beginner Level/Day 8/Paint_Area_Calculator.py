import math 

def area (height,weight,cover):
    num_of_cans = (height*weight)/cover
    round_of_cans = math.ceil(num_of_cans)
    print(round_of_cans)


h = int(input("Input the Height\n"))
w = int(input("Input the Weight\n"))
coverage = 5

area (height=h,weight=w,cover=coverage)