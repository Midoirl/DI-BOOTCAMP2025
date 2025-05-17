#Challenge 1: Sorting
#Write a program that sorts words in alphabtical order separated by commas
words = ((input("Enter 4 words separated by commas ")).split(",")) #split the string each time a comma starts and store in a variable
#words is now a list, now sort this list in alphabatical order
sorted_list = sorted(words) #now we have a sorted list with the strings in alphabetical order
#Now we want to take the sorted words in the list, and join them  by  "," so that they're all re separated by , and store that all in a variable
sorted_strings = ",".join(sorted_list)
print(sorted_strings) #print back the sorted strings separated by commas

#Challenge 2: Longest word
#Write a function that takes a sentence as input and returns the longest word in the sentence,
#Step 1: Define the function that takes a string (the sentence) as a parameter
def longest_word(the_sentence):
    
    #Step 2: Split the sentence into words and store into a variable words
    words_list = the_sentence.split(" ") #now words is a list with the split words inside it
    #Store a variable to store each word and keep updating it with the higher character word
    biggest_word = ""
    #Iterate through the words using a for each word in the word_list loop 
    for word in words_list:
        if len(word) > len(biggest_word):
            #Update the the word variable with the bigger word 
            biggest_word = word
            
    return biggest_word
        
#Call the function that deduces the longest word
print(longest_word("A thing of beauty is a joy forever"))
    

    




    
    
    
    





    
 