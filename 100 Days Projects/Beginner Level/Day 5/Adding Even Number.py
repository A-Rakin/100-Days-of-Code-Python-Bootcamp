num = int(input("Enter the Number you want to calculate the sum. This will be our target!!\n"))

even_num = 0

for i in range(2,num+1,2):
    even_num += i
    
print(even_num)