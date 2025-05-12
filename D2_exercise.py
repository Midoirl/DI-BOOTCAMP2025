#Ex1
my_fav_numbers = {7,10,4,2}
new_numbers = {1,5,6} 
#Add 1,5,6 to the set , my_fav_numbers becomes{1, 2, 4, 5, 6, 7, 10}
my_fav_numbers.update(new_numbers) 
friend_fav_numbers = {3,14,12,11}
#Cojoin my_fav_numbers and friend_fav_number
my_fav_numbers.update(friend_fav_numbers) 
#Create our_fav_numbers as an empty set
our_fav_numbers = set() 
our_fav_numbers.update(my_fav_numbers)
print(our_fav_numbers)
#Our_fav_numbers becomes the unifed set for me and my friends favorite numbers


#Ex2
t = (5,4,2,1)
t += (3,)
print(t)

#Ex3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Remove Banana from basket
basket.remove("Banana")
#Remove Blueberries from basket
basket.remove("Blueberries")
#Basket is now ["Apples", "Oranges"]
#Add Kiwi to the end of the list
basket.append("Kiwi")
#Basket is now ["Apples", "Oranges", "Kiwi"]
basket.insert(0,"Apples")
#Basket is now ['Apples', 'Apples', 'Oranges', 'Kiwi']
#Count how many times "Apples" appears in basker
print(basket.count("Apples"))
#Clear basket of fruits
basket.clear()
print(basket)


#Ex4
list_integers = [] #Create an empty list
i = 1.0
while i < 5:
    if i == int(i): #if i is the same value as its integer value
        list_integers.append(int((i))) #add the int to the list
    else:
        list_integers.append(i) # add the float to the list 
    
    i+= 0.5 #increment by 0.5 each time
print(list_integers)

#Ex5
#loop to print all numbers from 1 to 20
for i in range(1,21): # (i=0; while i <= 20 : i++)
        print(i)
for i in range(1,21):  #Second for loop where it only prints even numbers
    if i % 2 ==0: 
        print(i) 

#Ex6
while True:
    name = input("Write your name: ")
    if name == "mido": 
        break 
    else:
        continue #goes back to the start of the loop
    
#Ex7
#Ask user for input of fav fruits separated by spaces, split them each time a space is entered and convert to list
fruits = list(input("Enter your favorite fruits separated by spaces: ").split())
#Ask the user for the name of any fruit
any_fruit = input("Enter the name of any fruit: ")
if any_fruit in fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
    
#Ex8
#Store state as true
toppings = []
state = True
pizza_price = 10
while state == True:
    topping = input("Enter the pizza toppings one by one: ")
    print("Type 'quit' if that's all the toppings ")
    toppings.append(topping) #Add topping to list 
    if topping != ("quit"):
        print(f"Adding {[topping]}  to your pizza.")
        pizza_price += 2.50 #increment price
    if topping == ('quit'):
        toppings.remove("quit")
        state = False

print(toppings)
print(f"The total cost of your pizza is {pizza_price}$")

#Ex9
state = True
price = 0
while state == True:
    age = int(input("Enter the ages of each person in the family: "))
    if age < 3:
        price += 0 
    elif age >= 3 and age <=12:
        price += 10
    else:
        price += 15
    
    all_or_not = input("Is that all? Type 'yes' or 'no' ")
    if all_or_not == "yes":
        state = False
    elif all_or_not == "no":
        continue

print (f"Your total ticket cost is {price}$ ")

#Ex9 Bonus
list_of_teenagers = []
state = True 
while state == True:
    print("List all the attendees for the restricted movie")
    name = (input("What's your name?: "))
    age = int(input("What's your age? "))
    if 16 <= age <= 21:
        list_of_teenagers.append(name)
    
    all_or_not2 = input("Is that all? Type 'yes' or 'no' ")
    if all_or_not2 == "yes":
        state = False
    elif all_or_not2 == "no":
        continue

print(f"The qualified attendees to watch the film are {list_of_teenagers}")

#Ex10

sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
finished_sandwiches = []
for sandwich in sandwich_orders:
    if ("Pastrami") in sandwich_orders:
        sandwich_orders.remove("Pastrami") 
    print(f"I have made your {sandwich} sandiwch")

finished_sandwiches.append(sandwich_orders)
    
print(finished_sandwiches)
        
        
        

    
    
    
    






    
