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

guessed_letters = []
guessed_letter = ""
count = 0
hangman = IDK.x.selecting_hangman()
	

class CustomButton(Button,IDK): #blueprint for my special buttons that delete themselves on touch
    def on_touch_down(self, touch):
        global count
        global guessed_letters
        global guessed_letter
        if self.collide_point(*touch.pos): #if touched
            print(f"\nCustomButton.on_touch_down: text/id={self.id}")
            guessed_letter = self.id  #the guessed letter used for logic is the id of the button
            guessed_letters.append(guessed_letter) #add that letter to the list of used letters for logic
            count =  IDK.x.test_guessed_letter(guessed_letter, hangman, count) #sees if it was right or wrong and adjusts count accordingly
            self.parent.ids.btn_rep.text = IDK.x.nitty_gritty(hangman, guessed_letter, guessed_letters) #the representation of all the letters guessed
            
            if count == 1:
                self.parent.ids.new_image.source = 'hangmanpic1.png'
            elif count == 2:
                self.parent.ids.new_image.source = 'hangmanpic2.png'
            elif count == 3:
                self.parent.ids.new_image.source = 'hangmanpic3.png'
            elif count == 4:
                self.parent.ids.new_image.source = 'hangmanpic4.png'
                self.parent.add_widget(Button(text = "YOU LOSE"))
                sm.current = "forth"
            if count != 4:
                self.parent.remove_widget(self) #suicides itself
            return True    # consumed on_touch_down & stop propagation / bubbling
        return super(CustomButton, self).on_touch_down(touch)


class WindowManager(ScreenManager):
	pass
class MainWindow(Screen):
	pass
class SecondWindow(Screen,mh):
	pass
class ThirdWindow(Screen, IDK):

	def __init__(self, **kwargs):
		super(ThirdWindow, self).__init__(**kwargs)
		self.create_buttons()

	def create_buttons(self): #properties of each button
		k = .65
		j = .3
		c = 0
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		for letter in alphabet:
			a = CustomButton(id = letter, text= letter, pos_hint = {'x': k, 'y':j}, size_hint = (.05,.1))
			self.add_widget(a)
			c +=1
			k += .05
			if c == 7:
				j -= .1
				k = 0.65
				c = 0	
class ForthWindow(Screen,mh):
	pass
	
sm = WindowManager()
sm.add_widget(MainWindow())
sm.add_widget(SecondWindow())
sm.add_widget(ThirdWindow())
sm.add_widget(ForthWindow())

class HangmanApp(App):
	def build(self):
		Window.clearcolor = (1, 0, 0, 1)
		return sm


if __name__ == '__main__':
	HangmanApp().run()
