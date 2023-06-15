#This is a minigame to begin with python :)
import time
print("-------------------------- WELCOME TO THE TREASURE ISLAND --------------------------\n")
time.sleep(5)
print("Now, you are in a lake. On the right is a small village. On the left is a forest.")
print(r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     || 
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-' ''')
left_right1=input("Which side do you want to move, l (left) or r (right)? ")
if left_right1=="l":
	print("You are in a dark forest.")
	time.sleep(5)
	print("In front, you hear a river flowing.")
	time.sleep(5)
	print("On the right is emitting light of an unknown origin.")
	time.sleep(5)
	straight_right2=input("Do you want to go straight or turn right? s (straight) or r (right)? ")
	if straight_right2=="s":
		print("You were going straight.")
		time.sleep(5)
		print("Suddenly a bear lunged forward, devouring you.")
		time.sleep(5)
		print("You died.")
		time.sleep(3)
		print("GAME OVER!")
	else:
		print("The closer you get, the brighter the light.")
		time.sleep(5)
		print("You can see a big pit.")
		time.sleep(5)
		print("Congrats! You've got a pit full of gold.")
		time.sleep(3)
		print("You WIN!.")
else:
	print("The village is very beautiful with a chocolate house and\nsome cake trees. It's really great!")
	time.sleep(5)
	print("But in the chocolate house, there is an old woman is \ncalling you in for a drink.")
	time.sleep(5)
	go_run2=input("Do you want to g(go) into the house or r(run) to another place? ")
	if go_run2=="g":
		print("The old woman invites you to drink milk.")
		time.sleep(5)
		print("You drank it and ...")
		time.sleep(3)
		print("died")
		time.sleep(3)
		print("GAME OVER!")
	else:
		print("You run to the left.")
		time.sleep(5)
		print("You see the light and get close to it.")
		time.sleep(5)
		print("Congrats! You've got a pit full of gold.")
		time.sleep(3)
		print("You WIN!.")
print("\n-------------------------------------END--------------------------------------------")