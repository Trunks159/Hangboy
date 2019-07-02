def test_guessed_letter(guess, secret_word):
    return guess in secret_word

def make_placeholder(hangman, guessed_letter, guessed_letters):
	placeholder = ""
	for letter in hangman: 
		if guessed_letters != []:
			j = 1
			for guessed_letter in guessed_letters: #goes through each letter in bank
				if letter == guessed_letter: 
					placeholder += guessed_letter
					break
				elif (letter != guessed_letter) and (j == len(guessed_letters)):
					placeholder += " _"
				j += 1
		else: 
			placeholder += "_ "		
				
	return placeholder



