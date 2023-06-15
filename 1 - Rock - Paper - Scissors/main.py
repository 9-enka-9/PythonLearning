import random
import time
print("------------------- WELCOME TO THE ROCK-PAPER-SCISSORS GAME -------------------")
rock='''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''
scissors='''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
rps=[rock,paper,scissors]
choice=int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors.\n"))
print(f"Your choice is:\n{rps[choice]}")
time.sleep(2)
ai_choice=random.randint(0,2)
print(f"My choice is:\n{rps[ai_choice]}")
win_lose="You win, I lose."
lose_win="You lose, I win."
time.sleep(1)
if ai_choice == 0 and choice == 1:
	print(win_lose)
elif ai_choice == 1 and choice == 0:
	print(lose_win)
elif ai_choice == 1 and choice == 2:
	print(lose_win)
elif ai_choice == 2 and choice == 1:
	print(lose_win)
elif ai_choice == 2 and choice == 0:
	print(win_lose)
elif ai_choice ==0 and choice == 2:
	print(lose_win)
else:
	print("We are even.")
print("-------------------------------------------------------------------------------")
