#Input a Python List of Student Heights
heights = input("Enter student heights separated by spaces: ").split()

# Convert each input string to an integer
for i in range(0,len(heights)):
    heights[i] = int (heights[i])


# Calculate total height
total_heights = 0

for sum in heights:
    total_heights+=sum

print(f"The total Height is: {total_heights}") 

# Count number of students
number_of_students = 0

for student in heights:
    number_of_students+=1
    
print(f"The total student is:{number_of_students}")      

#calculate Average
average = total_heights/number_of_students

print(f"Average is: {average}")