#Ex1
#Goal, create a function that displays a message about what you're learning.
#Step 1: Define a function to display message
def display_message():
    print("I am learning about functions in Python.")

#Call the function 
display_message()

#Ex2
#Goal, create a function that displays a message about a favorite book.
#Define a function named favorite_book()
def favorite_book(title):
    print(f"One of my favorite books is {title}.")
#Call the function with an argument
favorite_book("American Prometheus")

#Ex3
#Goal: Create a function that describes a city and its country
#function should accept two parameters city and country consecutively
def describe_city(city,country = "Unknown"): #Give country parameter a defult value "Unknown"
    #Step 2: print a message
    print(f"{city} is in {country}.")
#Call the function with two arguments
describe_city("Dublin","Ireland") #Output would be Dublin is in Ireland.
#Call the function with one argument only which is the city
describe_city("Jerusalem") #Output would be Jerusalem is in Unknown.
#this is due to default value being set to Unknown  so when no arguments are passed to the country, it prints out the defult value

#Ex4
#Import the random Module
import random
#Define a function with a parameter that accepts a number between 1 and 100 as a parameter
def random_checker(number):
    #Generate a random int between 1 and 100 and store in a variable
    random_number = random.randint(1,100)
    #Compare the numbers, if they are the same print a sucess message
    if random_number == number:
        print("Success!, the numbers match")
    #Otherwise print a fail message and display both numbers
    else:
        print(f"Fail! Your number: {number}, Random number: {random_number}")
    
#Call the function with a number between 1 and 100
random_checker(4)

#Ex5
#Define a function called make_shirt with two parameters size and text
#Modify make_shirt so that size has a default value of "large" and text has "I love Python"
def make_shirt(size = "large",text = "I love Python"):
    #Set up the function to display a sentence summerizing the shirt's size and message
    print(f"The size of the shirt is {size} and the text is {text}.")
    
#Call make_shirt() to make a large shirt with the default message.
make_shirt()
#Call make_shirt() to make a medium shirt with the default message.
make_shirt("medium")
#Call make_shirt() to make a shirt of any size with a different message.
make_shirt("extra small","functions are fun")
#Step 6 (Bonus): Keyword Arguments
make_shirt("small","Hello!")

#Ex 6
#Step 1: Create a List of Magician Names
magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]
#Step 2: Create a Function that takes magician_names as a paremter to Display Magicians
def show_magicians(magician_names):
    #Iterate through list and print each magician's name
    for magician in magician_names:
        print(magician) 
    
# Create a Function to Modify the List
def make_great(magician_names):
    # Use a for loop to iterate through the list and add “the Great” before each magician’s name.
    return[name + " the Great" for name in magician_names]
        #Clear and add it to the magician_names variable
    
#Call make_great() to modify the list
magician_names = make_great(magician_names)
#Call show_magicians() to display the modified list
show_magicians(magician_names)

#Ex7
#Goal: Generate a random temperature and provide advice based on the temperature range.
#Step 1 create the get_random_temp() function
# Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.
#Modify random_temp to return a floating point number
def get_random_temp():
    return float(random.uniform(-10,40))

#Create a function called main() 
def main():
    #Call get_random_temp() to get a random temperature and store it in a variable
    temp = (get_random_temp())
    print(f"The temperature right now is {temp} degrees Celsius")
    #Provide temp based advice 
    #Case 1: temp below 0c
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.") 
    #Case 2: temp between 0c and 16c 
    elif 0 <= temp <= 16:
        print("Quite chilly! Don’t forget your coat.")
    #Case 3: temp between 16c and 23c
    elif 16 <= temp <= 23:
        print("Nice weather.")
    #Case 4 : temp between 24c and 32c
    elif 24 <= temp <= 32:
        print("A bit warm, stay hydrated.")
    #Case 5 : temp between 32c and 40c
    elif 32 <= temp <= 40:
        print("It's really hot! Stay cool.")
    

main()
    
    
    
    





        
    
    
    

    
    




    
    




    

    
    