# Import the AnagramChecker class from my other file
from anagram_checker import AnagramChecker

#Step 1:
#Show a menu, offering the user to input a word or exit.
#Keep showing the menu until the user chooses to exit.
def main():
    #Create a checker obj from AnagramChecker
    checker = AnagramChecker()

    while True:
        #Print menu options
        print("\nMenu:")
        print("1. Input a word")
        print("2. Exit")
        
        #Get user choice as input
        choice = input("Choose an option: ")
        
        #Step 2:
        #If the user chooses to exit, break out of the loop
        if choice == "2":
            print("Goodbye!")
            break
        
        #Step 3:
        #If the user chooses to input a word
        elif choice == "1":
            #Ask the user for a word
            user_input = input("Enter a word: ")
            
            #Remove whitespace from start and end
            word = user_input.strip()
            
            #Step 4:
            #Check if only a single word is entered (Hint: split by spaces and check length)
            if len(word.split()) != 1:
                print("Error: Please enter only ONE word.")
                continue
            
            #Step 5:
            #Check if only alphabetic characters (no numbers, no special characters)
            if not word.isalpha():
                print("Error: Only alphabetic characters are allowed.")
                continue

            #Step 6:
            #Check if the word is valid (use AnagramChecker)
            if checker.is_valid_word(word.lower()):
                print(f'\nYOUR WORD: "{word.upper()}"')
                print("This is a valid English word.")
            else:
                print(f'\nYOUR WORD: "{word.upper()}"')
                print("This is NOT a valid English word.")
            
            #Step 7:
            #Find all possible anagrams (use AnagramChecker)
            anagrams = checker.get_anagrams(word.lower())
            #Display the anagrams in a user-friendly way
            if anagrams:
                print("Anagrams for your word:", ", ".join(anagrams))
            else:
                print("No anagrams found for your word.")
        
        #Step 8:
        #If user enters an invalid menu option
        else:
            print("Error: Please select a valid option (1 or 2).")

#Step 9:
#Run the main function if this file is executed directly
if __name__ == "__main__":
    main()