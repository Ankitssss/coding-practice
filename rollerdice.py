import random

num_dice = int (input("how many dice are rolling"))
num_sides = int (input("how many sides on each dice"))

while True:
    for die in range(num_dice):
      print(random.randint(1,num_sides))
    reply = input("Roll again ? ()")
    if reply =="q":
       break