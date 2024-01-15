import random


rock ="RRRRRRRRRRR"
paper ="PPPPPPPPPPPPP"
scissor ="SSssssssss"

num=random.randint(1,3)

if num == 1:
    comp_move = "rock"
elif num == 2:
    comp_move = "paper"
elif num == 3:
    comp_move = "scissor"

player_move = input("Enter your move (rock, paper, or scissors): ").lower()
print("your Move---")
if player_move=="rock":
    print(rock)
elif player_move=="paper":
    print(paper)
elif player_move=="scisor":
    print(scissor)
