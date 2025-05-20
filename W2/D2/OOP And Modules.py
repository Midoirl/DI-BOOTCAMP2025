#Ex1
class Currency():
    def __init__(self,currency,amount):
        self.currency = currency
        self.amount = amount
    
    #Modify the str method to display the amount of money with its currency
    def __str__(self):
        return(f"{self.amount} {self.currency}")
    
    #Modify the int method to display the amount of money
    def __int__(self):
        return(self.amount)
    
    #Modify the repr method 
    def __repr__(self):
        return(f"{self.amount} {self.currency}")
    
    #Modify the __add__ method
    def __add__(self,other): #Take other as another object
        #Check if the other.amount is an int, in that case add it
        if isinstance(other,int): #If in instance the other parameter is an int
            return self.amount + other
            
        
        #Check if the other amount has the same currency
        elif isinstance(other,Currency):
            if self.currency == other.currency: #IF in instance the other parameter is a currency
                return self.amount + other.amount
            else: #If currency types dont match
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>.")
    
    #Moidfy the __idadd__ method
    def __iadd__(self,other):
        #Check if the other.amount is an int , in that cass increment it
        if isinstance(other,int):
            self.amount += other
            #Update the self.amount
            return self
        elif isinstance(other,Currency):
            if self.currency == other.currency:
                self.amount += other.amount
                return self
            else: #Else raise a type error
                raise TypeError(f"Cannot increment between Currency type {self.currency} and {other.currency}.")
        
c1 = Currency('dollars', 5)
c2 = Currency('dollars', 10)
c3 = Currency('shekels', 1)
c4 = Currency('shekels', 10)

print(str(c1))
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1) 
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

#print(c1+c3)
#TypeError: Cannot add between Currency type <dollar> and <shekel>

#Ex 3, in other files

#Ex 4
import datetime

#Make a function that displays the current date
def display_current_date():
    date_now = datetime.datetime.now()
    return(date_now)
#Display current date
print(display_current_date())

#Ex 5
#Create a function that displays the amount of time left until January 1st
#Display the current time and store it in now
now = display_current_date()
#Make a datetime object for january 1st of the year
next_jan_1 = datetime.datetime(now.year + 1, 1, 1)
#Time difference 
time_difference = next_jan_1 - now
print(time_difference)

#Ex 6
#Create a function that accepts a birthdate as an argument and displays a message stating how many minutes the user has lived in his life
def minutes(birthdate):
    time_spent = datetime.datetime.strptime(birthdate, "%d/%m/%Y") 
    now = display_current_date() #Displays current time
    difference = now - time_spent#Subtstracts now from birthdate
    print(difference.total_seconds()) #Returns the total number of seconds lived

#Call function
(minutes("10/02/2006"))

#Ex 7: 
from faker import Faker #import the faker class
#Create a fake instance
fake = Faker()
#Create an empty list of users 
users = []
#Create a function to add users
def add_users(number_of_users):
    for user in range(number_of_users): #For each user in the n of users
        #Create a dictionary with these keys
        fake_dict = {"name": fake.name(),
         "address": fake.address(),
         "language_code": fake.language_code()
        }
        #Append the user dictionary to the users list
        users.append(fake_dict)
    return users

#Call the function and print the users list
fake_data = add_users(4) #Add 4 users
print(fake_data)
        
        
    

    

    
    
    