import random


def play_round():
    computer_move = ""
    random_index = random.randint(0, 2)
    if random_index == 0:
        computer_move = "r"
    elif random_index == 1:
        computer_move = "p"
    elif random_index == 2:
        computer_move = "s"

    player_move = input("Enter (r)ock, (p)aper, or (s)cissors: ").lower()
    while player_move not in ["r", "p", "s"]:
        player_move = input("Invalid input. Enter r/p/s: ").lower()

    if player_move == computer_move:
        return "draw"
    elif (
        (player_move == "r" and computer_move == "s")
        or (player_move == "p" and computer_move == "r")
        or (player_move == "s" and computer_move == "p")
    ):
        return "win"
    elif (
        (player_move == "r" and computer_move == "p")
        or (player_move == "p" and computer_move == "s")
        or (player_move == "s" and computer_move == "r")
    ):
        return "loss"


# --------Main-------
print("=== Rock, Paper, Scissors! ===")

keep_playing = True
wins = 0
losses = 0
ties = 0

while keep_playing:
    round_outcome = play_round()
    if round_outcome == "win":
        wins += 1
    elif round_outcome == "loss":
        losses += 1
    else:
        ties += 1

    print("Current score:\n" + str(wins), "wins,", losses, "losses,", ties, "ties.")

    continue_response = input("Do you want to continue? (y)es or (n)o: ").lower()
    while continue_response not in ["y", "n"]:
        continue_response = input("Invalid input! Enter y/n: ").lower()

    if continue_response == "n":
        print("Thanks for playing. Goodbye and have fun!")
        
        print(f"Final result: {wins} wins, "
              f"{losses} losses, {ties} ties.")
        
        keep_playing = False