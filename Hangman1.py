import random
import sys
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
class ManHangs():
	prompt = """Hello my good sir or mam, or animal or alien or whatever you\nare. My name is Jordan, and we're gonna play hangman cus I suck\nat programming and only know how to make this game.\nI'm sure you know how to play it already though.\nHere's a representation of how many letters there are: """
	#	letter_representation()
	def print_prompt(self):
		w = Button(text = "Hii")
		app.root.current.add_widget(w)
	def func(self):
		c = input("Would you like to continue? y/n\n")
		if c == "n":
			print("That's unfortunate...")
			sys.exit(0)
		else:
			print("Let's get this show on the road then! ")

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
		
		definitions = {1: "first", 2:"second", 3:"third", 4:"forth"}
		
		if guess not in secret_word: #if guessed is wrong, add to counter
			count += 1
			print("That was the " + definitions[count] + " time bro!")
		if count == 0: #shows how close user is to losing
			print("""       
							_____
						   |     |
								 |
								 |
								 |
								 |
				_________________|_________
			""")
		elif count == 1:
			print("""       
							_____
						   |     |
						   O     |
								 |
								 |
								 |
				_________________|_________
			""")
		elif count == 2:
			print("""       
							_____
						   |     |
						   o     |
						   |     |
								 |
								 |
				_________________|_________
			""")
		elif count == 3:
			print("""       
							_____
						   |     |
						   o     |
						  /|\    |
								 |
								 |
				_________________|_________
			""")
		elif count == 4:
			print("""       
							_____
						   |     |
						   o     |
						  /|\    |
						  / \     |
								 |
				_________________|_________
			""")
		return count

	def nitty_gritty(self, hangman, guessed_letter, guessed_letters):
		print("Al the nitty gritty is under this: \n")
		print(hangman)
		print(guessed_letter)
		print(guessed_letters)
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
			print("This is set_in: ")
			print(set_in)
		return set_in


def main():

	active_2 = True
	while active_2:
		prompt_user()
		guessed_letters = [] #sets up a bank of all the letters the user has tried
		active = True #flag
		counter = 0
		while active: #main game
			 #higher the counter goes, the closer you are to losing, passed tto test letter
			
			guessed_letter = input("Guess a letter: ") #asks the user for a letter
			counter = test_guessed_letter(guess = guessed_letter, secret_word = hangman, count = counter)
			#tests letter for certain things
			if counter == 4:
				a = input("You lose... Do you wanna play again?")
				break
			
			guessed_letters.append(guessed_letter) #adds to bank of used letters

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

			print(set_in)
			if set_in == hangman:
				print("You won!!")
				break
		a = input("Do you wanna play again??:")
		if a == "y":
			continue
		else:
			break
