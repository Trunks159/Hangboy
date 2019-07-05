import random	
	
def test_guessed_letter(guess, secret_word):
	count = "right"
	if guess not in secret_word: #if guessed is wrong, add to counter
		count = "wrong"
	return count




