import kivy
import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from kivy.graphics import Color, Rectangle, Line
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from os import path

words = ["cat", "dog", "bird", "falcon", "hawk", "eagle"]


def make_placeholder(word, guesses): #takes secret word and all past guesses and returns a new word with dashes in unguessed letters
	placeholder = ""
	for letter in word: 
		if guesses:	
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
	
def false_count(log):
	i  = 0
	for item in log:
		if item == False:
			i+=1
	return i
	
Builder.load_file("hangman_v2.kv")

class WindowManager(ScreenManager):
	pass
	
class StartWindow(Screen):
	pass

class Game(Screen):	
	hangman = ObjectProperty(random.choice(words))
	guesses = ObjectProperty(None)
	current = ObjectProperty(None)
	tf_log = ObjectProperty(None)
	main_image = ObjectProperty("")
	placeholder = ObjectProperty("")
	deleted_buttons = ObjectProperty("")
	turns = ObjectProperty(7)
	skull_colors = ObjectProperty()
	count = ObjectProperty(0)

	def __init__(self, **kwargs):
		super(Game, self).__init__(**kwargs)
		self.guesses = []
		self.tf_log = []
		self.deleted_buttons = []
		self.skull_colors = []
		self.placeholder = make_placeholder(self.hangman, self.guesses)	
		self.skulls = self.create_skulls()
		self.create_alphabuttons()
		
	def on_main_image(self, instance, value):
		self.ids.im.source = value
		
	def on_placeholder(self, instance, value):
		self.ids.place.text = value
		
	def on_count(self, instance, value):
		self.skulls[value - 1].color = [1,0,0,1]
		self.update_pic(value)
		self.update_screen_color(value)
				
	def create_skulls(self):
		skulls = []
		for i in range(self.turns): #creates 7 skull images, their position is centered throught the formula
			skull = Skull(color = [1,1,1,1])
			skull.pos_hint = {'x':(skull.size_hint[0]* i) +( (1 - skull.size_hint[0]*7)/2), 'y': .58}
			self.ids.layout.add_widget(skull)
			skulls.append(skull)
		return skulls	
		
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
			self.ids.layout.add_widget(a)
			print(a)
			c +=1
			k += a.size_hint[0]
			if c == cwants:
				j -= a.size_hint[1]
				k = start
				c = 0	
			
	#def update_skulls(self,c): #returns new list instead of changing 1 element of list
	#	self.skull_colors = [1,0,0,1]
		#i = 0 
		#new_list = []
		#for skull in self.skull_colors:
		#	if i == c-1:
		#		new_list.append([1,0,0,1])	
		#	else:
		#		new_list.append(skull)
		#	i+=1 
		#self.skull_colors = new_list
		
	def update_pic(self,c):
		if c == g.turns:	#when you've reached that point
			sm.current = "lose"	#lose screen
		else:
			if path.exists("Pictures/" + str(c) + ".gif"):			#these change the main picture
				self.main_image = "Pictures/" + str(c) + ".gif"
			else:
				self.main_image = "Pictures/" + str(c) + ".jpg"	
					
	def update_screen_color(self,c):
		Window.clearcolor = [1,1 - (1/self.turns*c),0,1]		#window color change based on how many wrong answers there are		

	def process_guess(self, guess):

		if len(guess) < 1:
			self.guesses.append(guess)	
			self.current = self.guess in self.hangman
			if current == False : self.placeholder = make_placeholder(self.hangman, self.guesses) 
		else:
			self.current = guess == self.hangman
			if self.current: sm.current = "win" 
			
		self.tf_log.append(self.current)
		self.count = false_count(self.tf_log)

		if '_' not in g.placeholder: sm.current = "win" 

		
			
class Win(Screen):
	pass	


class Lose(Screen):
	pass
		


class AlphaButton(Button): #blueprint for my special buttons that delete themselves on touch		
				
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            g.guess = self.id  
            g.process_guess(g.guess)
            btn_info = {"text" : self.text, id : self.id, "pos_hint" : self.pos_hint, "size_hint": self.size_hint} #stores info of button in dictionary before destroying itself
            g.deleted_buttons.append(btn_info)
            self.parent.remove_widget(self)
            
            
class Skull(Image):
	pass


sm = WindowManager()
sm.add_widget(StartWindow())
g = Game()
sm.add_widget(g)
sm.add_widget(Win())
sm.add_widget(Lose())

class HangmanApp(App):
	
	def build(self):
		Window.clearcolor = [1, 1, 0, 1]
		Window.size = (540, 960)
		Window.left = 0
		Window.top = 25

		return sm


if __name__ == '__main__':
	HangmanApp().run()
