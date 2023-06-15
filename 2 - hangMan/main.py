import random
import hangman_art
import hangman_wordslist
from os import system

_=system("cls")

print(hangman_art.logo)
print("\n------------------------------------------------------------------") 
chosen_word=random.choice(hangman_wordslist.word_list)
blank=[]
count=6

for _ in chosen_word:
	blank.append("_")

while not count == 0:
	guess=input("Please guess a letter: ").lower()
	n2=0
	
	for letter in chosen_word:
		n2+=1
		if letter == guess:
			blank[n2-1]=letter
	
	if guess not in chosen_word:
		count-=1
		print(f"You're wrong. Now the word is: {' '.join(blank)}")
	else:
		print(f"Right! Now the word is: {' '.join(blank)}")
	print(hangman_art.stages[count])
	
	if ''.join(blank) == chosen_word:
		print("YOU WIN!")
		print("------------------------------------------------------------------")
		break
	elif count>0:
		print("------------------------------------------------------------------")
		n=0
		for alpha in hangman_wordslist.alphabet:
			if guess == alpha:
				hangman_wordslist.alphabet[n]='_'
			n+=1	
		print("\nYou can guess these letters: ")
		print(' '.join(hangman_wordslist.alphabet) + '\n')

if not ''.join(blank) == chosen_word:
	print(f"YOU LOSE! The correct answer is: {chosen_word}")