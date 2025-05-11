#Ex1
print("Hello world \n" *4 ) 

#Ex2
print(99**3 *8)

#Ex3
#1) False
#2) True
#3) False
#4) TypeError as > is not supported between strings and integers
#5) False

#Ex4
computer_brand = ("I have a <computer_brand> computer.")
print(computer_brand)

#Ex5
name = ("Mido")
age = 19
shoe_size = 43
info = (f"Hi, my name is {name}, I'm {age} years old and my shoe size is {shoe_size}, one interesting fact about myself is that I love problem solving  ")
print(info)

#Ex6
a = 5
b = 3 
if a > b:
    print("Hello World ")
    
#Ex7
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")

#Ex8
name = input("What's your name: ").lower()
if name == "mido":
    print("Omg we are twins we have the same name")
else:
    print("We arent twins :( ")

#Ex9
height = int(input("What's your height in centimeters: "))
if height > 145:
    print("You are tall enough to ride")
else:
    print("You need to grow some more to ride")