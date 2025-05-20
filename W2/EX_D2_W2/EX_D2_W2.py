#Exercises XP D2/W2

#Ex1 
#Create a pet class
# Step 0: Create the Pets class
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

# Step 1: Create the Cat base class
class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return (f'{self.name} is just walking around')

# Step 2: Subclasses
class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Now Siamese class 
class Siamese(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)  # inherit name and age properly

    def sing(self, sounds):
        return f'{sounds.upper()}!!!'  
    
    
    
bengal_cat = Bengal("Luna", 2)
chartreux_cat = Chartreux("Milo", 3)
siamese_cat = Siamese("Simba", 4)

all_cats = [bengal_cat, chartreux_cat, siamese_cat] # Store them all in a list
#Create a Pets instance of the list of cat instances
sara_pets = Pets(all_cats)
#Now take the cats for a walk
sara_pets.walk()

#Ex 2: Dogs
#Crate a Dog class with methods for barking, running , speed and fighting
class Dog:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
        
    #Implement a bark() method that returns "is barking"
    def bark(self):
        return "is barking"
    #Implement a run_speed() method that returns weight/ age * 10
    def run_speed(self):
        return self.weight / self.age * 10
    #Implement a fight(other_dog) method that returns a string indicating which dog won the fight based on run_speed * weight
    def fight(self,other_dog):
        if (self.run_speed() * self.weight) > (other_dog.run_speed() * other_dog.weight):
            return(f"{self.name } won the fight")
        else:
            return(f"{other_dog.name } won the fight")

#Create three instances with differnet names age and weight
dog1 = Dog("Rocky",10,0.3)
dog2 = Dog("Smockey",1,0.5)
dog3 = Dog("Pog",11,4)

#Call the methods to test
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2)) #Dog 2 wins the fight, then goes to dog 3
print(dog2.fight(dog3)) #Dog 3 wins the fight

#Ex 3: Dogs domesticated
#Continue from other file

#Ex 4
# Define a Person class to represent each family member
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""  # Last name will be assigned by the Family class

    def is_18(self):
        # Return True if the person is 18 or older, otherwise False
        return self.age >= 18

# Define a Family class to manage family members
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []  # List to hold Person instances

    def born(self, first_name, age):
        # Create a new person with the given first name and age
        person = Person(first_name, age)
        # Assign the family's last name to the person
        person.last_name = self.last_name
        # Add the new person to the family's members list
        self.members.append(person)
        print(f"{first_name} {self.last_name} was born into the family.")

    def check_majority(self, first_name):
        # Search for a family member by first name
        for member in self.members:
            if member.first_name == first_name:
                # Check if the member is 18 or older
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends.")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        # If no member is found with the given name
        print(f"No family member named {first_name} was found.")

    def family_presentation(self):
        # Print the family’s last name
        print(f"Family Name: {self.last_name}")
        print("Members:")
        # Print each member’s name and age
        for member in self.members:
            print(f"- {member.first_name} {member.last_name}, Age: {member.age}")



# Create a Family instance
kirresh_family = Family("Kirresh")

 # Add family members
kirresh_family.born("Mahmod", 11)
kirresh_family.born("Dana", 28)
kirresh_family.born("Ahmad", 38)

    # Check who is allowed to go out
kirresh_family.check_majority("Mahmod")
kirresh_family.check_majority("Dana")
kirresh_family.check_majority("Ahmad")

    # Show family presentation
kirresh_family.family_presentation()


        
            
        
        
            

            
        
