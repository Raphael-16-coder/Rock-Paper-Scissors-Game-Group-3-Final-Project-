import random

# Course: Data Structures and Algorithms
# Project Type: Group Programming Project
# Language: Python
# Interface: Console based
# Group 3 - Baltazar, Blaza, Garcia, Nieva, Malaybalay, Rabara
# BSIT 2-1

# AI Assistance Disclosure:
# This project used AI tools as reference and support.
# The final code was reviewed, understood, and implemented by the group.

# Dictionary to "store scores" (O(1) access)
scores = {
    "Player": 0,
    "Computer": 0,
    "Draws": 0
}

# List to store "match history" (O(n) traversal)
match_history = []

# Dictionary defining "game rules" (O(1) lookup)
rules = {
    "Rock": "Scissor",
    "Scissor": "Paper",
    "Paper": "Rock"
}

round_counter = 1


# THE MENU
def display_menu():
    print("\n===== Rock Paper Scissor Game Menu =====")
    print("1. Play a round")
    print("2. View score")
    print("3. View match history")
    print("4. Search match by round number")
    print("5. Reset game")
    print("6. Exit")


# PLAYING A ROUND
def play_round():
    global round_counter

    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")

    choice = input("Enter choice (1-3): ").strip()

    if choice not in ["1", "2", "3"]:
        print("❌ Invalid input. Please choose 1, 2, or 3.")
        return True

    player_choice = ["Rock", "Paper", "Scissor"][int(choice) - 1]
    computer_choice = random.choice(["Rock", "Paper", "Scissor"])

    result = determine_winner(player_choice, computer_choice)
    update_scores(result)

    # Storing The match data
    match_history.append({
        "round": round_counter,
        "player": player_choice,
        "computer": computer_choice,
        "result": result
    })

    print(f"\nRound {round_counter}")
    print(f"Player chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    print(f"Result: {result}")

    round_counter += 1

    # Will ask the player if they want to play another round
    return ask_play_again()

#  PLAY AGAIN
def ask_play_again():
    while True:
        print("\n" + "-" * 30)
        print("Do you want to play another round?")
        print("1. Yes")
        print("2. No")

        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            print("\n" + "=" * 30)
            print("Starting new round...")
            print("=" * 30)
            return True
        elif choice == "2":
            print("\nReturning to main menu...")
            return False
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")


#  DETERMINING THE WINNER (O(1))
def determine_winner(player, computer):
    if player == computer:
        return "Draw"
    elif rules[player] == computer:
        return "Player Wins"
    else:
        return "Computer Wins"


#  UPDATING THE SCORES (O(1))
def update_scores(result):
    if result == "Player Wins":
        scores["Player"] += 1
    elif result == "Computer Wins":
        scores["Computer"] += 1
    else:
        scores["Draws"] += 1


#  VIEWING THE SCORES
def view_scores():
    print("\n===== Current Scores =====")
    print(f"Player Wins: {scores['Player']}")
    print(f"Computer Wins: {scores['Computer']}")
    print(f"Draws: {scores['Draws']}")


# VIEW THE MATCH HISTORY (O(n))
def view_history():
    if not match_history:
        print("\nNo matches played yet.")
        return

    print("\n===== Match History =====")
    for match in match_history:
        print(
            f"Round {match['round']}: "
            f"Player={match['player']}, "
            f"Computer={match['computer']} → "
            f"{match['result']}"
        )


#  SEARCHING A MATCH (LINEAR SEARCH O(n))
def search_match():
    if not match_history:
        print("\nNo match history available.")
        return

    try:
        round_number = int(input("Enter round number to search: "))
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        return

    for match in match_history:
        if match["round"] == round_number:
            print("\nMatch Found!")
            print(f"Round: {match['round']}")
            print(f"Player: {match['player']}")
            print(f"Computer: {match['computer']}")
            print(f"Result: {match['result']}")
            return

    print("❌ No match found for that round.")


# WILL RESET THE GAME
def reset_game():
    global round_counter
    scores["Player"] = 0
    scores["Computer"] = 0
    scores["Draws"] = 0
    match_history.clear()
    round_counter = 1
    print("\nGame has been reset.")


# THE MAIN PROGRAM LOOP ( MENU )
def main():
    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            while play_round():
                pass
        elif choice == "2":
            view_scores()
        elif choice == "3":
            view_history()
        elif choice == "4":
            search_match()
        elif choice == "5":
            reset_game()
        elif choice == "6":
            print("\nThank you for playing! 👋")
            break
        else:
            print("❌ Invalid menu choice. Please try again.")


# PROGRAM ENTRY POINT
if __name__ == "__main__":
    main()
