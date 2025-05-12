#Challenge 1:
#Create an empty multiplication table
multiplication_table = []
number = int(input("Enter a number: "))
multiplication_table.append(number) #Add the number to the multiplication table
multiplied_number = number 
length = int(input("Enter a length: "))


for i in range(1,length): #loop through each number until the inputted length
    
    multiplied_number += number #for e.g 7 is inputted as number , 7+7, 14+7  21 + 7 and so on until the length
    multiplication_table.append(multiplied_number)

print(multiplication_table)

#Challenge 2:
#Initiallize empty set
string = input("Enter a string: ") 
unique_char = [] # store unrepeated characters

char_listed = list(string)

for char in char_listed:
    if char not in unique_char:
        unique_char.append(char)
        
result = ''.join(unique_char)
print(result)
        
        
        

    
        





    

