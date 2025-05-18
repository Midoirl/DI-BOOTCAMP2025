#Exercise 1: Cats
class Cat:
    def __init__(self,cat_name,cat_age):
        self.name = cat_name
        self.age = cat_age
        
#Step 1: Create 3 cat instances/ onjects 
cat1 = Cat("Lucy",7) #Cat name is lucy and age is 7
cat2 = Cat("Tommy",5) #.etcc
cat3 = Cat("Zeus",10044) 
#Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1,cat2,cat3):
    oldest_cat = cat1 #Initalize with the first cat
    #Create an if condition to loop through each cat instances and update oldest_cat variable only if it is older
    for cat in (cat1,cat2,cat3): #Loop through each cat
        if cat.age > oldest_cat.age:
            oldest_cat = cat #New cat
    
    return oldest_cat # Return back the oldest cat
            
oldest_cat = ((find_oldest_cat(cat1,cat2,cat3)))
#Print out the oldest cat details
print(f"The oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old.")

#Exercise 2: Dogs
class Dog:
    def __init__(self,dog_name,dog_height ):
        self.name = dog_name
        self.height = dog_height
        

    #Create a bark() method
    def bark(dog):
        print(f"{dog.name} goes woof!")
    #Create a jump() method
    def jump(dog):
        print(f"Jumps {dog.height *2} cm high!")
        
davids_dog = Dog("Sarah",10 )
sarahs_dog = Dog("David",4)
#Print dog Details (name and height) of each dog
print(vars(davids_dog))
print(vars(sarahs_dog))

#Use the bark and jump methods on the different dogs
davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
davids_dog.jump()
#Compare dog sizes?????

#Ex 3: Who's the song Producer
class Song: 
    def __init__(self,lyrics): #Take lyrics(list) as a parameter
        self.lyrics = lyrics
    
    #Create a sing_me_a_song() method that prints eaech element of the lyrics list on a  new line
    def sing_me_a_song(self):
        for lyric in self.lyrics:
            print(lyric) #For each individual lyric in lyrics , print lyric on an ew line
            

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

#Ex 4: Define the Zoo Class
#Initialize an empty list of animals to keep track

class Zoo:
    def __init__(self,zoo_name): 
        self.name = zoo_name
        self.animals = []
        #Add a method add_animal(new_anmial)
    def add_animal(self,new_animal):
            #if animal is not already in the list, append it to the animals list
        if new_animal not in self.animals:
            (self.animals).append(new_animal)
        #Add a method get_animals(), this prints out all the animals currently in the zoo
    def get_animals(self):
            print(*self.animals) # * unpacks the list and prints the elements inside it (all animals currently in the zoo)
        #Add a method sell_animal(animal_sold)
    def sell_animal(self,animal_sold): #Checks if a specified animal exists on the animals list and if so remove it from list
            if animal_sold in self.animals:
                (self.animals).remove(animal_sold)
        #Add a method sort_animals()
    def sort_animals(self):
        #Sort the animals alphabatically
        sorted_animals = sorted(self.animals)
        grouped_animals = {} #Initalize grouped animals
        for animal in sorted_animals: #For each animal in sorted_animals
            if animal[0] not in grouped_animals: #If the animal is not already in the grouped animals dictionary
                grouped_animals[animal[0].upper()] = [animal] #Assign the Letter upper case key to the animal list value
            else:
                grouped_animals[animal[0].upper()].append(animal) # Else just append the list containing the animal list with the assigned letter
        return grouped_animals #Return the grouped animals dictionary
    
    #Add a method get_groups()
    def get_groups(self):
        filtered_group = {}
        #Method prints the grouped animals that are created by sort_animals()
        grouped = self.sort_animals()
        #Loop through each letter and its corresponding list, if length list contains more than 1 , only return that 
        for letter, animals in grouped.items():
            if len(animals) > 1:
                filtered_group[letter] = [animals]

        print(filtered_group)
            
        
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Step 3: Use the Zoo methods
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Gorilla")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Bear")
ramat_gan_safari.get_animals()
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()



          
                
           
        
        

    

        
    



        
        
                
            
        
        
            
            
            
        
        
        
    





    
    





