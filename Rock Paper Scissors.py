def rock_paper_scissors(choice1,choice2):
    print("""The game is:
    -Rock-
    -Paper-
    -Scissors-
    """)
    while True:
        p1move = input(f"{choice1} choose: ")
        p2move = input(f"{choice2} choose: ")
        if p1move.lower() == "rock" and p2move.lower() == "scissors":
            print(f"{choice1} is the winner")
            break
        if p2move.lower() == "rock" and p1move.lower() == "scissors":
            print(f"{choice2} is the winner")
            break
        # Foarfeca VS Hartie
        if p1move.lower() == "scissors" and p2move.lower() == "paper":
            print(f"{choice1} is the winner!")
            break
        if p2move.lower() == "scissors" and p1move.lower() == "paper":
            print(f"{choice2} is the winner!")
            break
        # Hartie vs Piatra
        if p1move.lower() == "paper" and p2move.lower() == "rock":
            print(f"{choice1} is the winner!")
            break
        if p2move.lower() == "paper" and p1move.lower() == "rock":
            print(f"{choice2} is the winner")
            break
        if p1move.lower() == p2move.lower():
            print("Equal")

