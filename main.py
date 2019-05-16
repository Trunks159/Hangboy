import kivy
from Hangman1 import ManHangs as mh
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

Builder.load_file("yourpops.kv")

class IDK(): #makes an instance of the ManHangs class'mh'
	x = mh()
	
class WindowManager(ScreenManager):
	pass
class MainWindow(Screen):
	pass
class SecondWindow(Screen,mh):
	pass
class ThirdWindow(Screen, IDK):

	count = 0
	set_in = ''
	hangman = ObjectProperty(IDK.x.selecting_hangman()) #runs the selecting hangman method, converts string to object property
	hangman2 = ObjectProperty("                Hit For \nRepresentation of Word")
	guessed_letter = ObjectProperty(None)
	guessed_letters = []

	
	def call_method(self, count):
		self.count = IDK.x.test_guessed_letter(self.guessed_letter.text, self.hangman, self.count)
	
	def call_method_2(self):
		IDK.x.print_prompt()
	def call_method_3(self, set_in):
		self.set_in = IDK.x.nitty_gritty(self.hangman, self.guessed_letter.text, self.guessed_letters)
		self.ids.set.text = self.set_in
	def btn(self):
		blank_rep = IDK.x.letter_representation(self.hangman) #takes hangman, runs it through this function, stores in blank_rep
		self.hangman2 = blank_rep #updates hangman2 when this btn method is called
	def btn_2(self, guessed_letter, guessed_letters):
		guessed_letter = self.guessed_letter.text #updates the guessed letter from the text the user typed
		guessed_letters.append(guessed_letter) #adds to list of guessed letters
		


		
sm = WindowManager()
sm.add_widget(MainWindow())
sm.add_widget(SecondWindow())
tw = ThirdWindow()
sm.add_widget(tw)


class HangmanApp(App):
	def build(self):
		return sm


if __name__ == '__main__':
	HangmanApp().run()
