#Dictionary 
#Ex1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# Use the zip function to zip keys and corresponding values together and convert into a dict
dict1 = dict(zip(keys,values))

#Ex2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#Loop through each value in the family dict and use conditionals to calculate the total cost , also make an empty int for total cost to initalize and increment later
total_cost = 0
each_cost = {}
for name, age in family.items(): #.values gives the values of the specified dict values
    if age < 3: #First condtion
        cost = 0
        each_cost[name] = (f"{cost}$") #Assign the name key to each cost in the new dict to tell how much it costs for each person in dollars
        
    elif 3 <= age <= 12: #Second condition
        cost = 10
        each_cost[name] = (f"{cost}$") 
        total_cost += 10
        
    else:
        cost = 15 #Last condition
        each_cost[name] = (f"{cost}$")
        total_cost += 15
        
print(each_cost)
print(f"The total cost is {total_cost}$")

#Ex3
zara_info ={ "name": "Zara",
"creation_date": 1975,
"creator_name": "Amancio Ortega Gaona",
"type_of_clothes": ["men", "women", "children", "home"],   
"international_competitors": ["Gap", "H&M", "Benetton"],
"number_stores": 7000,
"major_color":{
    "France": "blue", 
    "Spain": "red", 
    "US": ("pink", "green")
}
}

#Change the value of number_stores from 7000 to 2
zara_info["number_stores"] = 2 #new value
#Print a sentence describing Zara's clients using the type_of_clothes key, create variable to store type of clothes as str
type_of_clothes = ", "
print(f"Zara has many type of clothes including clothes for {type_of_clothes.join(zara_info['type_of_clothes'])}")
#Add a new key country_creation with the value Spain.
zara_info.update({"country_creation":"Spain"})
#Check if international_competitors exists and, if so, add “Desigual” to the list.
if ("international_competitors") in zara_info:
    zara_info["international_competitors"].append("Desigual")
#Delete the creation_date key.
del zara_info["creation_date"]
#Print the last item in international_competitors.
print(zara_info["international_competitors"][-1])
#Print the major colors in the US.
print(zara_info["major_color"]["US"])
#Print the number of keys in the dictionary.
print (len(zara_info.keys()))
#Print all keys of the dictionary.
print(zara_info.keys())
    

#Ex4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# Initialize 3 empty dicts 
chars_to_index = {}
index_to_char = {}
sorted_char_to_index = {}
    
#1 Create a dictionary that maps characters to their indices:
for i, char in enumerate(users):
    chars_to_index[char] = i #character key to index value
print(f"Characters to indicies: {chars_to_index}")
  
#2 Create a dictionary that maps indices to characters:
for i, char in enumerate(users):
    index_to_char[i] = char #index key to character value
print(f"Characters to indicies: {index_to_char}") #we do the same thing as above but instead of assigning each char to i , we assign each i to char
#3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
sorted_users = sorted(users) #now we have a sorted list based on alphabatical order
for i, char in enumerate(sorted_users):
    sorted_char_to_index[char] = i #character key to index value
print( f"Alphabetically sorted characters to indicies:{sorted_char_to_index}")
    


    
    




        
        
    




    
    
    