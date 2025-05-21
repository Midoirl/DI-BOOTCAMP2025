#Day 3 Daily challenge (Topic, Dictionarys)

#Daily challenge 1
#Create a dictionary that stores the indices (number of the position) of each letter in a word provided by the user(input()).
#Ask the user to enter a word and store it in a variable
word = (input("Enter a word: "))
# Create an empty dictionary to store chars and indicies
dict_word = {}
#Iterate through each index and character of the input word using a for loop

for i,char in enumerate(word):
    #Case 1, if character is already a key in the dictonary, append the current index to the list assosiacted with that key
    if char in dict_word:
        dict_word[char].append(i)
    else:
        #Case 2 , if it is not, create a new key value pair in the dictionary
        dict_word[char] = [i]

#Expected output for dict_word, “dodo”, the output should be: {"d": [0, 2], "o": [1, 3]}.
print(dict_word)

#Daily challenge 2
#Create a program that prints a list of items that can be purchased with a given amount of money given these dicts
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
list_affordable = []
wallet = "$300"
#Data Cleaning:
#remove $ sign from wallet and convert it into an int so that we compare values
wallet_int = int(wallet.replace("$",""))
# Loop through each item, clean the price, and compare it to wallet value
# Add affordable items to the list
for item ,price in items_purchase.items():
    price_int = int(price.replace("$","").replace(",",""))
    if price_int < wallet_int:
        list_affordable.append(item) #Append the affordable items to the list
        
if list_affordable == []:
    print("Nothing")   
else: 
    print(sorted(list_affordable)) #Sort the final list in alphabetical order
    

    
    


    
    

    

