import random


def userchoice():
    while True:
        user_choice = (
            input("Enter your choice (rock, paper, or scissors): ").strip().lower()
        )
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            return print("Invalid choice. Please choose rock, paper, or scissors.")


def computerchoice():
    choices = ["rock", "paper", "scissors"]
    randdomChoice = random.choice(choices)
    print(f"the computer`s choice is {randdomChoice}")
    return randdomChoice


def detirminewinner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"


def updatescores(scores, winner):
    if winner == "user":
        scores["user"] += 1
    elif winner == "computer":
        scores["computer"] += 1
    else:
        scores["draw"] += 1
    return scores


def displayscores(scores):
    print(f"User:{scores['user']} | computer:{scores['computer']}|Draws:{scores['draw']}")


def play_again():
    choice = input("Do you want to play again? (yes/no):").strip().lower()
    return choice.startswith("y")


def main():
    scores = {"user": 0, "computer": 0, "draw": 0}
    while True:
        user_choice = userchoice()
        computer_choice = computerchoice()
        detirmine_winner = detirminewinner(user_choice, computer_choice)
        update_scores = updatescores(scores, detirmine_winner)
        displays_cores = displayscores(scores)

        if not play_again():
            break
    print("Thank you for playing Rock, Paper, Scissors!")


if __name__ == "__main__":
    main()
