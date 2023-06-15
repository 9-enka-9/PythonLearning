from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def caesar(cipher_direction, start_text, shift_number):
	end_text=""
	if cipher_direction=="decode":
		shift_number*=-1
	for letter in start_text:
		if alphabet.count(letter)>0:
			index=alphabet.index(letter)
			index+=shift_number
			if cipher_direction=="encode":
				while index>=26:
					index-=26
			else:
				while index<0:
					index+=26
			end_text+=alphabet[index]
		else:
			end_text+=letter
	print(f"The {direction}d text is {end_text}")
caesar(cipher_direction=direction, start_text=text, shift_number=shift)
again=input('Type "yes" if you want to run again. Otherwise type "no"\n').lower()
while again=="yes":
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	caesar(cipher_direction=direction, start_text=text, shift_number=shift)
	again=input('Type "yes" if you want to run again. Otherwise type "no"\n').lower()
print("Goodbye!")