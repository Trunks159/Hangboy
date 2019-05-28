import random

class ManHangs():
	prompt = """Hello my good sir or mam, or animal or alien or whatever you\nare. My name is Jordan, and we're gonna play hangman cus I suck\nat programming and only know how to make this game.\nI'm sure you know how to play it already though.\n"""
	#	letter_representation()



	def selecting_hangman(self):
		word_collection = ["soda", "izze", "compile", "build"] #collection of words the computer can choose from
		hangman = random.choice(word_collection) #randomly chooses a word
		return hangman
	def letter_representation(self, hangman): #blank representation of word
		set_in = ""
		for letter in hangman:
			set_in += "_ "
		return set_in
	
	def test_guessed_letter(self, guess, secret_word, count):
		if guess not in secret_word: #if guessed is wrong, add to counter
			count += 1
		return count

	def nitty_gritty(self, hangman, guessed_letter, guessed_letters):
		if guessed_letters == []:
			set_in = self.letter_representation(hangman)
		else:
			set_in = ""
			for letter in hangman: # MOST DIFFICULT PART OF THE PROGRAM TO CONSTRUCT
				j = 1

				for guessed_letter in guessed_letters: #goes through each letter in bank
					if letter == guessed_letter: 
						set_in += guessed_letter
						break
					elif (letter != guessed_letter) and (j == len(guessed_letters)):
						set_in += " _"
					j += 1
		return set_in


