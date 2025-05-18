# Step 1: Create the Farm class
class Farm:
    # Step 2: Initialize the farm with a name and an empty dictionary for animals
    def __init__(self, farm_name):
        self.name = farm_name  # Store the name of the farm
        self.animals = {}      # Dictionary to hold animals and their counts

    # Step 3: Method to add animals to the farm
    def add_animal(self, animal_type, count=1):
        # If the animal already exists, just increase the count
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            # Otherwise, add it to the dictionary with the given count
            self.animals[animal_type] = count

    # Step 4: Method to return a formatted string with farm info
    def get_info(self):
        # Start with the farm name
        output = f"{self.name}'s farm\n\n"
        # List each animal and how many there are
        for animal, count in self.animals.items():
            output += f"{animal} : {count}\n"
        # Add the signature line
        output += "\n    E-I-E-I-0!"
        return output

    # Step 6 (Bonus): Return a sorted list of all animal types
    def get_animal_types(self):
        return sorted(self.animals.keys())

    # Step 7 (Bonus): Return a short summary sentence with pluralized animal names
    def get_short_info(self):
        animal_list = self.get_animal_types()  # Get sorted list of animal names
        animal_strings = []

        # Add 's' to animal names if there are more than one
        for animal in animal_list:
            if self.animals[animal] > 1:
                animal_strings.append(animal + 's')
            else:
                animal_strings.append(animal)

        # Format the sentence nicely depending on how many animals there are
        if len(animal_strings) == 1:
            animals_str = animal_strings[0]
        else:
            animals_str = ", ".join(animal_strings[:-1]) + " and " + animal_strings[-1]

        return f"{self.name}'s farm has {animals_str}."


# Step 5: Testing the class with some example animals
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)       # Add 5 cows
macdonald.add_animal('sheep')        # Add 1 sheep
macdonald.add_animal('sheep')        # Add another sheep (total 2)
macdonald.add_animal('goat', 12)     # Add 12 goats

# Print the full farm info
print(macdonald.get_info())

# Print the short summary
print(macdonald.get_short_info())
