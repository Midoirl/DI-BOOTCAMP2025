from EX_D2_W2 import Dog
import random

# Create a class PetDog that inherits from Dog
class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        # Initialize parent attributes
        super().__init__(name, age, weight)
        # New attribute to indicate if the dog is trained
        self.trained = trained

    def train(self):
        # Print the dog's bark and mark it as trained
        print(f"{self.name} {self.bark()}")
        self.trained = True

    def play(self, *args):
        # Gather all the dog names involved in play
        dog_names = [self.name] + [dog.name for dog in args if isinstance(dog, Dog)]
        print(f"{', '.join(dog_names)} all play together!")

    def do_a_trick(self):
        # Only do a trick if trained
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            trick = random.choice(tricks)
            print(f"{self.name} {trick}")
        else:
            print(f"{self.name} isn't trained yet.")

#Create instances
rex = PetDog("Rex", 5, 20)
luna = PetDog("Luna", 3, 15)
max = PetDog("Max", 4, 18)

#Methods
rex.train()
rex.play(luna, max)
rex.do_a_trick()