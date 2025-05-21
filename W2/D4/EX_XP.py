import random

#Create a function named get_words_from_file that takes the file path as an argument
def get_words_from_file(file_path): #Take the file path as an argument
    #Open the file in read mode("r")
    file = open(file_path, "r")
    #Read the file content
    content = file.read()
    #Split the content into a list of words
    list_content = content.split()
    #Return the list of words
    return list_content

#Step 2: Create the random_sentence function
def get_random_sentence(sentence_length): #Takes the length of sentence as an argument
    list_of_word = get_words_from_file("DI-BOOTCAMP2025\W2\D4\words.txt")
    #Initalize empty lsit
    random_words = []
    #Use a loop that runs sentence_length times.
    for word in range(sentence_length):
        random_word= random.choice(list_of_word) #Choose a random word from the list of words
        random_words.append(random_word) #For each random word append to the empty list
    
    selected_words = " ".join(random_words) #Join all the words as strings
    #Make selected words lowercase and return it
    return selected_words.lower()

#Step 3: Create the main function
def main():
    while True:
        #Print a short message explaining the program
        print("This program generates a random sentence from words in a file!")
        #Ask for user input
        try:
            user_length = int(input("How long do you want your sentence to be?(Choose between 2 and 20): "))
            #Validate the input, make sure its between 2 and 20 
            
            #Only in the scenario that the user types an int and is within the range
            if (2 <= user_length <= 20):
                print(get_random_sentence(user_length))
                break

            else:
                print("Please enter a number within the specified range")
        
        except ValueError:
            print("Please type a valid number:")

#Call main()
main()

#Ex 2
#Import the json module
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

#convert this json string into a python dict
data = json.loads(sampleJson)
#Dump the dict into a json file
with open("output.json","w") as file:
    json.dump(data, file , indent=4)

#Access the salary key using nested dictionary access
salary = data["company"]["employee"]["payable"]["salary"]
#print value of salary key
print(salary)
#Add a new- value pair to the employee dict
data["company"]["employee"]["birth_date"] = "2006-02-10"

#Now modify to output.json
with open("output.json","w") as file:
    json.dump(data,file,indent=4)

    





        

    

    





    

