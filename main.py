import kivy
from Hangman1 import ManHangs as mh
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
import time

Window.size = (540, 960)
Window.left = 0
Window.top = 25

Builder.load_file("yourpops.kv")



class GameState():
	def __init__(self):
		self.y = mh()
		self.guessed_letters = [] #bank of letters guessed, global variable
		self.guessed_letter = "" # keeps track of the last guessed letter
		self.count = 0 #how many times user has been wrong
		self.hangman = self.y.selecting_hangman() #randomly selects hangman
		self.deleted_buttons = [] #bank of letters used/deleted
		self.current_color = [1,1,0,1]
		self.skull_colors = []
		for i in range(7):
			self.skull_colors.append([1,1,1,1])
		self.main_image_source = ""
		self.btn_rep_default = self.y.nitty_gritty(self.hangman, self.guessed_letter, self.guessed_letters)




class CustomButton(Button): #blueprint for my special buttons that delete themselves on touch
				
    def on_touch_down(self, touch):
        #all of these above will be used
        if self.collide_point(*touch.pos): #if touched
           # print(f"\nCustomButton.on_touch_down: text/id={self.id}")
            gs.guessed_letter = self.id  #the guessed letter used for logic is the id of the button
            gs.guessed_letters.append(gs.guessed_letter) #add that letter to the list of used letters for logic
            gs.count =  gs.y.test_guessed_letter(gs.guessed_letter, gs.hangman, gs.count) #sees if it was right or wrong and adjusts count accordingly
            self.parent.btn_rep.text = gs.y.nitty_gritty(gs.hangman, gs.guessed_letter, gs.guessed_letters) #the representation of all the letters guessed
            if '_' not in self.parent.btn_rep.text: #if all letters are filled out, go to the win screen
                sm.current = "forth"
            self.parent.wrong(gs.count)
            if gs.count != 7:
                btn_info = {"text" : self.text, id : self.id, "pos_hint" : self.pos_hint, "size_hint": self.size_hint} #stores info of button in dictionary before destroying itself
                gs.deleted_buttons.append(btn_info) #adds the dictionary to a list
                self.parent.remove_widget(self) #suicides itself

		

class WindowManager(ScreenManager):
	pass
	
class MainWindow(Screen):
	pass
		
class ThirdWindow(Screen):

	def __init__(self, **kwargs):
		super(ThirdWindow, self).__init__(**kwargs)
		
		f = RelativeLayout()
		self.create_buttons()
		self.btn_rep =((Label(text= GameState().btn_rep_default, font_size = 30, color = (1,1,1,1), size_hint =  (.3, .05), pos_hint = {'x':.325,'y':.5})))
		self.add_widget(self.btn_rep)
		self.main_image = Image(source = GameState().main_image_source, size_hint = (.6,.7), pos_hint = {'x':.2, 'y': .5}, allow_stretch = True)
		self.add_widget(self.main_image)	
		self.add_widget(f)
		self.skulls = []
		for i in range(7): #creates 7 skull images, their position is centered throught the formula
			im = Image(source = "Pictures/Skull.png", color = GameState().skull_colors[i], allow_stretch = True, keep_ratio = True, size_hint = [.1,.1])
			im.pos_hint = {'x':(im.size_hint[0]* i) +( (1 - im.size_hint[0]*7)/2), 'y': .58}
			self.skulls.append(im)
			f.add_widget(im)
			
		


	def create_buttons(self): #properties of each button
		borders = [.01,.01]
		start = borders[0]

		k = start
		j = .3
		c = 0
		cwants = 10
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		for letter in alphabet:
			a = CustomButton(id = letter, text= letter, pos_hint = {'x': k, 'y':j}, size_hint = ((1-sum(borders))/cwants,.15))
			
			self.add_widget(a)
			c +=1
			k += a.size_hint[0]
			if c == cwants:
				j -= a.size_hint[1]
				k = start
				c = 0	
		

		
	def restore_buttons(self): 
		for button in gs.deleted_buttons:
			self.add_widget(CustomButton(id = button["text"], text= button["text"], pos_hint = button["pos_hint"], size_hint = button["size_hint"]))
			print("TEST: " , button["text"])
	
	def wrong(self, c):
		turns = 7
		if c == turns:
			sm.current = "fifth"
		else:

			if path.exists("Pictures/" + str(c) + ".gif"):
				self.main_image.source = "Pictures/" + str(c) + ".gif"
			else:
				self.main_image.source = "Pictures/" + str(c) + ".jpg"
			self.skulls[c-1].color = [1,0,0,1]
			

			Window.clearcolor = [1,1 - (1/turns*c),0,1]
		
class ForthWindow(Screen):
	def test(self):
		global guessed_letters
		global guessed_letter 
		global hangman  
		global count
		hangman = y.selecting_hangman()
		count = 0
		guessed_letter = ""
		guessed_letters = []
		s3 = self.manager.get_screen("third")
		s3.restore_buttons()
		s3.btn_rep.text = "Secret Word" 
		s3.new_image.source = "hangmanpic0.png"
			
class FifthWindow(Screen):
	def test(self):
		global guessed_letters
		global guessed_letter 
		global hangman  
		global count
		hangman = y.selecting_hangman()
		count = 0
		guessed_letter = ""
		guessed_letters = []
		s3 = self.manager.get_screen("third")
		s3.restore_buttons()
		s3.btn_rep.text = "Secret Word" 
		s3.new_image.source = "hangmanpic0.png"
gs = GameState()
sm = WindowManager()
sm.add_widget(MainWindow())
sm.add_widget(ThirdWindow())
sm.add_widget(ForthWindow())
sm.add_widget(FifthWindow())

class HangmanApp(App):
	
	def build(self):
		Window.clearcolor = [1, 1, 0, 1]
		current_color = Window.clearcolor
		return sm


if __name__ == '__main__':
	HangmanApp().run()
