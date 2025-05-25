from game import Game

def get_user_menu_choice():
    """
    Display menu options and return user's validated choice.
    """
    options = {
        "1": "Play a new game",
        "2": "Show scores",
        "3": "Quit"
    }

    print("\nMenu:")
    for key, value in options.items():
        print(f"{key}. {value}")

    while True:
        choice = input("Select an option (1/2/3): ").strip()
        if choice in options:
            return choice
        print("Invalid choice. Please enter 1, 2, or 3.")

def print_results(results):
    """
    Display game summary.
    """
    print("\nGame Summary:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thanks for playing!")

def main():
    """
    Run the game menu loop.
    """
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "1":  # Play a new game
            game = Game()
            result = game.play()
            results[result] += 1

        elif choice == "2":  # Show scores
            print_results(results)

        elif choice == "3":  # Quit
            print_results(results)
            break

if __name__ == "__main__":
    main()
