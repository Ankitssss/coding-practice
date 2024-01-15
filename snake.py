import random

roll1 = random.randint(1,6)
roll2 = random.randint(1,6)
roll_count=1

while roll1 != 6 or roll2!=6:
    print(roll2 , roll1)
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    roll_count+=1

print(roll2 ,roll1)
print("YAHHH SNAKE KEY!!!!")
print(f"the total count of {roll_count}")