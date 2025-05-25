
import random



#1 class is a user-defined blueprint or prototype from which objects are created. It defines a set of attributes and methods.

# 2. An instance is a concrete object created based on the structure defined by a class.

# 3. Encapsulation is the concept of bundling data and methods that operate on that data within one unit, typically a class.

# 4. Abstraction means hiding complex implementation details and showing only the necessary features of an object.


# 5. Inheritance is a mechanism where a new class derives properties and behaviors (methods) from an existing class.

# 6.Multiple inheritance allows a class to inherit from more than one base class.

# 7. Polymorphism allows methods to do different things based on the object it is acting upon, even if they share the same name.

# 8.MRO defines the order in which Python looks for a method in a hierarchy of classes. It uses the C3 linearization algorithm.


#Exercise 2: 

class Card:
    def __init__(self, suit, value):
        # Initialize a card with a given suit and value
        self.suit = suit
        self.value = value

    def __repr__(self):
        # Provide a readable string representation of the card
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        """
        Initialize a new deck with all 52 unique cards.
        Each card is a combination of one suit and one value.
        """
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        """
        Shuffle the deck. If the deck has fewer than 52 cards,
        it is reconstructed to ensure a complete shuffle.
        """
        if len(self.cards) < 52:
            print("Deck is incomplete. Reinitializing before shuffling.")
            self.__init__()  # Rebuild the deck
        random.shuffle(self.cards)
        print("Deck shuffled.")

    def deal(self):
        """
        Remove and return one card from the top of the deck.
        If the deck is empty, return a message indicating no cards remain.
        """
        if not self.cards:
            return "No cards left to deal."
        return self.cards.pop()



#Creating an instance
if __name__ == "__main__":
    # Create a new deck and shuffle it
    deck = Deck()
    deck.shuffle()

    # Deal 5 cards from the shuffled deck
    print("\nDealing 5 cards from the deck:")
    for i in range(5):
        print(f"Card {i + 1}: {deck.deal()}")