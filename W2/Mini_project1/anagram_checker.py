import os
dir_path = os.path.dirname(os.path.realpath(__file__))

#Create a class called Anagram Checker
class AnagramChecker():
    #Step 1:
    #Modify init to return a list of the file
    def __init__(self, path = dir_path):
        #Initialize an empty list to store the words
        self.words = []
        #Open the file in read mode
        with open(f'{dir_path}/sowpods.txt', 'r', encoding='utf-8') as file_obj:
            #Loop through each word in file
            for word in file_obj:
                #Convert each clean word uppercased for consistency into a list
                clean_word = word.strip().lower() 
                #Append this clean word into self.words
                self.words.append(clean_word)

    #Step 2:
    #Make a method that checks if the given word is a valid word
    def is_valid_word(self,word): #Takes word as a parameter
        #Check if its valid
        if word in self.words:
            return True
        else:
            return False
    
    #Step 3:
    #Make helper method to compare word1 and word true
    def is_anagram(self,word1,word2):
        #If the two words are exactly identical , same order of chars, return false (thats not an engram thats just the same word)
        if word1 == word2:
            return False
        #If the sorted version of the words is the same, (but originally different order of letters was present) --> This is what an engram is
        elif sorted(word1) == sorted(word2):
            return True
        else:
            return False
        
    #Main method
    #Make a method that finds all anagrams for the given word
    #For example if the word of user is meat return list containing mate, tame.team
    def get_anagrams(self,word):
        #Initalize an empty list of engrams
        anagrams = []
        #Loop through each candidate for an engarm in the words list, and use the helper function
        for candidate in self.words:
            if self.is_anagram(word,candidate) == True:
                #append the candidate into engrams
                anagrams.append(candidate)
                #Return the list of engrams
        return anagrams
    
    
checker = AnagramChecker() #Create a checker obj
print(checker.is_valid_word("i"))       # True
print(checker.get_anagrams("pilates"))


    
        
        
        
    
    
    
    
    
    
    
    
    
    
 
            
        
    
        
        
        
        
        
    
    
    
        

        
        
            
            
        
        
        