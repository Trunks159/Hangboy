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
from kivy.core.window import Window

Builder.load_file("yourpops.kv")
class IDK():
	x = mh()


class CustomButton(Button):

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print(f"\nCustomButton.on_touch_down: text={self.text}")
            self.parent.remove_widget(self)
            return True    # consumed on_touch_down & stop propagation / bubbling
        return super(CustomButton, self).on_touch_down(touch)

class WindowManager(ScreenManager):
	pass
class MainWindow(Screen):
	pass
class SecondWindow(Screen,mh):
	pass
class ThirdWindow(Screen, IDK):

	count = 0
	hangman = ObjectProperty(mh().selecting_hangman()) #runs the selecting hangman method, converts string to object property
	blank_repr = ObjectProperty("                Hit For \nRepresentation of Word")
	guessed_letter = ObjectProperty(None)
	guessed_letters = []
	k = 0
	
	def __init__(self, **kwargs):
		super(ThirdWindow, self).__init__(**kwargs)
		self.create_buttons()

	def create_buttons(self):
		k = 0
		j = .6
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		for letter in alphabet:
			self.add_widget(CustomButton(text= letter, pos_hint = {'x':k, 'y':j}, size_hint = (.05,.1)))
			k += .05
			if k == (.05 * 6):
				j-=.1
				k = 0
				
				

	def test_guessed(self, count):
		self.count = mh().test_guessed_letter(self.guessed_letter.text, self.hangman, self.count)#tests the letter, returns count which has been added to if the letter wasnt in secret word
	def call_btn_rep(self):
		self.ids.btn_rep.text = mh().nitty_gritty(self.hangman, self.guessed_letter.text, self.guessed_letters)#returns a representation of all the letter guessed
	def call_btn_submit(self, guessed_letter, guessed_letters):
		guessed_letter = self.guessed_letter.text #updates the guessed letter from the text the user typed
		guessed_letters.append(guessed_letter) #adds to list of guessed letters
		self.ids.guessed_letter.text = ""
	def call_leftover_options(self, guessed_letters):
		possible_guesses = 'abcdefghijklmnopqrstuvwxyz'
		for guess in self.guessed_letters:
			if guess in possible_guesses:
				c = possible_guesses.replace(guess, "")
				self.ids.label_possible_guesses.text = c
			elif (guess not in self.guessed_letters) and (guess == guessed_letter):
				print ("You already guessed that...")
	def create_alphabuttons(self):
		alphabet = 'abcdefghijklmnopqrstuvwxyz'
		i = 0
		j = .2
		k = 0
		alphabutton = []
		for letter in alphabet:
			
			a = Button(text = letter, id = letter, size_hint = (.03, .05), pos_hint = {'x':i, 'y': j})
			alphabutton.append(a)
			self.add_widget(alphabutton[k])
			print(alphabutton[k].text)
			alphabutton[k].bind(on_press = self.do_stuff)
			k += 1
			i += .03
			if i == (.03*7):
				j-=.05
				i = 0
				
	def do_stuff(self, k):
		
		print(k)
		#self.remove_widget((self.alphabutton)[self.k])
		
		
sm = WindowManager()
sm.add_widget(MainWindow())
sm.add_widget(SecondWindow())
tw = ThirdWindow()
sm.add_widget(tw)


class HangmanApp(App):
	def build(self):
		Window.clearcolor = (1, 0, 0, 1)
		return sm


if __name__ == '__main__':
	HangmanApp().run()
