import kivy
import random
from random_word import RandomWords
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.graphics import Color, Rectangle, Line
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from os import path
r = RandomWords()
Window.size = (540, 960)
Window.left = 0
Window.top = 25

DELETEDBUTTONS

Builder.load_file("hangman.kv")

class InitialStates():
	def __init__(self):



		

class AlphaButton(Button): #blueprint for my special buttons that delete themselves on touch
				
    def on_touch_down(self, touch):
        #all of these above will be used
        if self.collide_point(*touch.pos): #if touched
           # print(f"\nCustomButton.on_touch_down: text/id={self.id}")
            gs.guessed_letter = self.id  #the guessed letter used for logic is the id of the button
            gs.guessed_letters.append(gs.guessed_letter) #add that letter to the list of used letters for logic
            gs.count = gs.guessed_letter in gs.hangman
            gs.count_log.append(gs.count) #sees if it was right or wrong and adjusts count accordingly
            self.parent.placeholder.text = gs.make_placeholder(gs.hangman, gs.guessed_letter, gs.guessed_letters) #the representation of all the letters guessed
            if '_' not in self.parent.placeholder.text: #if all letters are filled out, go to the win screen
                sm.current = "win"
                Window.clearcolor = [0,0,1,1]
            if gs.count == False:
                self.parent.wrong(gs.count_count_log())            
           # if gs.count_count_log() != 7:
            btn_info = {"text" : self.text, id : self.id, "pos_hint" : self.pos_hint, "size_hint": self.size_hint} #stores info of button in dictionary before destroying itself
            gs.deleted_buttons.append(btn_info) #adds the dictionary to a list
            self.parent.remove_widget(self) #suicides itself

class Skull(Image):
	pass

class WindowManager(ScreenManager):
	pass
	
class MainWindow(Screen):
	pass
		
class ThirdWindow(Screen):
	def __init__(self, **kwargs):
		super(ThirdWindow, self).__init__(**kwargs)
		self.hangman = r.get_random_word(maxLength = 7, hasDictionaryDef = True) #randomly selects hangman
		self.guesses = []
		self.guess = ""
		self.count_log = []
		self.count = ""
		self.deleted_buttons = [] #bank of letters used/deleted
		self.current_color = [1,1,0,1]
		self.skull_colors = []
		for i in range(7):
			self.skull_colors.append([1,1,1,1])
		self.main_image_source = ""
		self.placeholder = self.make_placeholder(self.hangman, self.guesses)
		self.create_alphabuttons()
		self.skulls = self.create_skulls()
		for skull in self.skulls:
			self.r.add_widget(skull)

	def create_alphabuttons(self): #properties of each button
		borders = [.01,.01]
		start = borders[0]
		k = start
		j = .3
		c = 0
		cwants = 10
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		for letter in alphabet:
			a = AlphaButton(id = letter, text= letter, pos_hint = {'x': k, 'y':j}, size_hint = ((1-sum(borders))/cwants,.15))
			self.add_widget(a)
			c +=1
			k += a.size_hint[0]
			if c == cwants:
				j -= a.size_hint[1]
				k = start
				c = 0	
				
	def create_skulls(self):
		skulls = []
		for i in range(7): #creates 7 skull images, their position is centered throught the formula
			skull = Skull(color = self.skull_colors[i])
			skull.pos_hint = {'x':(skull.size_hint[0]* i) +( (1 - skull.size_hint[0]*7)/2), 'y': .58}
			skulls.append(skull)
		return skulls
		

		
	def restore_buttons(self, buttons): 
		for button in buttons:
			self.add_widget(AlphaButton(id = button["text"], text= button["text"], pos_hint = button["pos_hint"], size_hint = button["size_hint"]))
			print("TEST: " , button["text"])
	
	def wrong(self, c):#changes main image, skull color, and window color
		turns = 7	#amount of times you can be wrong
		if c == turns:	#when you've reached that point
			sm.current = "lose"	#lose screen
		else:
			if path.exists("Pictures/" + str(c) + ".gif"):			#these change the main picture
				self.main_image.source = "Pictures/" + str(c) + ".gif"
			else:
				self.main_image.source = "Pictures/" + str(c) + ".jpg"
			self.skulls[c-1].color = [1,0,0,1]		#skull color change
			Window.clearcolor = [1,1 - (1/turns*c),0,1]		#window color change based on how many wrong answers there are
			
	def count_count_log(self, x): #returns amount of False in a list
		i = 0
		for element in x:
			if element == False:
				i += 1
		return i
		
	def make_placeholder(self, word, guesses): #takes secret word and all past guesses and returns a new word with dashes in unguessed letters
		placeholder = ""
		for letter in hangman: 
			if guesses:	#if guess
				j = 1
				for guess in guesses:
					if letter == guess: 
						placeholder += guess
						break
					elif (letter != guess) and (j == len(guesses)):
						placeholder += " _"
					j += 1
			else: 
				placeholder += "_ "			
		return placeholder				
		

		
			
class Win(Screen):
	def test(self):
		s3 = self.manager.get_screen("third")
		s3.restore_buttons(gs.deleted_buttons)
		gs.reset_everything()
		s3.placeholder.text = gs.third_screen_placeholder
		s3.main_image_source = ""
		Window.clearcolor = [1,1,0,1]
		for skull in s3.skulls:
			skull.color = [1,1,1,1]
	
	
			
class Lose(Screen):
	def __init__(self, **kwargs):
		super(Lose, self).__init__(**kwargs)
		self.ids.float.add_widget(Label(text = "The Secret Word Was: " + gs.hangman, size_hint = [.2,.2], pos_hint = {"bottom" : 1}))
		
	def test(self):
		print(gs.hangman)
		s3 = self.manager.get_screen("third")
		s3.restore_buttons(gs.deleted_buttons)
		gs.reset_everything()
		s3.placeholder.text = gs.third_screen_placeholder
		s3.main_image_source = ""
		Window.clearcolor = [1,1,0,1]
		for skull in s3.skulls:
			skull.color = [1,1,1,1]



sm = WindowManager()
sm.add_widget(MainWindow())
sm.add_widget(ThirdWindow())
sm.add_widget(Win())
sm.add_widget(Lose())

class HangmanApp(App):
	
	def build(self):
		Window.clearcolor = [1, 1, 0, 1]
		return sm


if __name__ == '__main__':
	HangmanApp().run()
