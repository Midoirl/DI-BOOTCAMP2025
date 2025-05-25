import random


class Game:
    def get_user_item(self):
        """
        Prompt the user to choose rock, paper, or scissors.
        Repeats until valid input is given.
        """
        choices = ["rock", "paper", "scissors"]
        while True:
            user_input = input("Choose rock, paper, or scissors: ").lower()
            if user_input in choices:
                return user_input
            print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")

    def get_computer_item(self):
        """
        Randomly select rock, paper, or scissors for the computer.
        """
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        """
        Determine the result of the game.
        Return 'win', 'loss', or 'draw'.
        """
        if user_item == computer_item:
            return "draw"

        win_conditions = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }

        if win_conditions[user_item] == computer_item:
            return "win"
        else:
            return "loss"

    def play(self):
        """
        Play a single round of the game.
        Get both choices, determine result, print outcome.
        Return the result.
        """
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"\nYou chose: {user_item}")
        print(f"Computer chose: {computer_item}")
        print(f"Result: {result.upper()}\n")

        return result

