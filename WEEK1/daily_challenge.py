#Daily Challenge
import random

string = input("Enter a string: ")
if len(string) < 10:
    print("String not long enough")
elif len(string) > 10:
    print("String too long")
else:
    print("Perfect string")
    first_char = string[0]
    last_char = string[-1]
    print(f"First character is {first_char} and Last character is {last_char}")
    for char in string:
        print(char)
    #Jumble the string
    char_list = list(string) 
    print(char_list)
    random.shuffle(char_list)
    result = ''.join(char_list)
    print(f"Original string: {string}")
    print(f"Shuffled string list: {(char_list)}")
    print(result)
    
    
    

