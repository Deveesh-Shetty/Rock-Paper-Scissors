import random

print("""Move:            
            R - Rock
            S - Scissors
            P - Paper""")
print("---x---x----x---x---x---x---x---x---x---x---x---x---x---")

list = ('R', 'P', 'S')
move = 0
comp_points = 0
user_points = 0
draws = 0

while move != "":
    move = input("Enter your move: ").upper()
    if move not in list:
        print("Enter either R, P, S")
        print("---x---x----x---x---x---x---x---x---x---x---x---x---x---")
        continue

    comp_move = random.choice(list)
    print("Computer chose: " + comp_move)

    if comp_move == move:
        print("It's a draw!")
        draws += 1
        print("---x---x----x---x---x---x---x---x---x---x---x---x---x---")
    elif move == 'S' and comp_move == 'R' or move == 'R' and comp_move == 'P' or move == 'P' and comp_move == 'S':
        print("Computer Wins")
        comp_points += 1
        print("---x---x----x---x---x---x---x---x---x---x---x---x---x---")
    elif move == 'P' and comp_move == 'R' or move == 'S' and comp_move == 'P' or move == 'R' and comp_move == 'S':
        print("User Wins")
        user_points += 1
        print("---x---x----x---x---x---x---x---x---x---x---x---x---x---")

print("User Points = " + str(user_points))
print("Computer Points = " + str(comp_points))
print("No. of Draws = " + str(draws))
