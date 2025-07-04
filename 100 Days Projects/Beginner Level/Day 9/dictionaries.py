programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop":"An action of doing something over and over again"}

print(programming_dictionary["Bug"])


#Adding new Items in the Dictionary
programming_dictionary ["if"] = "A Conditional Statement in a program"

print(programming_dictionary)

#Create an Empty Dictionary
empty_dictionary = {}

print(empty_dictionary)

#Edit an Item in the Existing Dictionary 
programming_dictionary["Bug"] = "A Moth in the Computer which create sufferings to the coders"

print(programming_dictionary)

#Loop Through a Dictionary

for key in programming_dictionary:
    print(key) #Itwill show only the key
    print(programming_dictionary[key]) #It will show the values 