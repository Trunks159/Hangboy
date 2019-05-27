import kivy
from Hangman1 import ManHangs as mh
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
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
deleted_buttons = []

class CustomButton(Button,IDK): #blueprint for my special buttons that delete themselves on touch
    def on_touch_down(self, touch):
        global count
        global guessed_letters
        global guessed_letter
        global deleted_buttons
        if self.collide_point(*touch.pos): #if touched
           # print(f"\nCustomButton.on_touch_down: text/id={self.id}")
            guessed_letter = self.id  #the guessed letter used for logic is the id of the button
            guessed_letters.append(guessed_letter) #add that letter to the list of used letters for logic
            count =  IDK.x.test_guessed_letter(guessed_letter, hangman, count) #sees if it was right or wrong and adjusts count accordingly
            self.parent.btn_rep.text = IDK.x.nitty_gritty(hangman, guessed_letter, guessed_letters) #the representation of all the letters guessed
         
            if '_' not in self.parent.btn_rep.text:
                sm.current = "forth"
            
            if count == 1:
                self.parent.new_image.source = 'hangmanpic1.png'
            elif count == 2:
                self.parent.new_image.source = 'hangmanpic2.png'
            elif count == 3:
                self.parent.new_image.source = 'hangmanpic3.png'
            elif count == 4:
                self.parent.new_image.source = 'hangmanpic4.png'
                sm.current = "fifth"
            if count != 4:
                btn_info = {"text" : self.text, id : self.id, "pos_hint" : self.pos_hint, "size_hint": self.size_hint}
                deleted_buttons.append(btn_info)
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
	global hangman

	def __init__(self, **kwargs):
		super(ThirdWindow, self).__init__(**kwargs)
		self.btn_rep = ""
		self.new_image = ""
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
		
		self.btn_rep =((Label(id = "btn_rep", text= "Secret Word", font_size = 30, color = (1,1,1,1), size_hint =  (.3, .3), pos_hint = {'x':.325-.15,'y':.2-.15})))
		self.add_widget(self.btn_rep)
		self.new_image = Image(source = 'hangmanpic0.png', size_hint = (.6,.7), pos_hint = {'x':.2, 'y': .32}, allow_stretch = True)
		self.add_widget(self.new_image)
		
	def restore_buttons(self): 
		global deleted_buttons
		for button in deleted_buttons:
			self.add_widget(CustomButton(id = button["text"], text= button["text"], pos_hint = button["pos_hint"], size_hint = button["size_hint"]))
			print("TEST: " , button["text"])

		
		
class ForthWindow(Screen):
	def test(self):
		global guessed_letters
		global guessed_letter 
		global hangman  
		global count
		hangman = IDK.x.selecting_hangman()
		count = 0
		guessed_letter = ""
		guessed_letters = []
		s3 = self.manager.get_screen("third")
		s3.restore_buttons()
		
	
class FifthWindow(Screen):
	def test(self):
		global guessed_letters
		global guessed_letter 
		global hangman  
		global count
		hangman = IDK.x.selecting_hangman()
		count = 0
		guessed_letter = ""
		guessed_letters = []
		s3 = self.manager.get_screen("third")
		s3.restore_buttons() 
		
	
sm = WindowManager()
sm.add_widget(MainWindow())
sm.add_widget(SecondWindow())
sm.add_widget(ThirdWindow())
sm.add_widget(ForthWindow())
sm.add_widget(FifthWindow())

class HangmanApp(App):
	
	def build(self):
		Window.clearcolor = (1, 0, 0, 1)
		return sm


if __name__ == '__main__':
	HangmanApp().run()
