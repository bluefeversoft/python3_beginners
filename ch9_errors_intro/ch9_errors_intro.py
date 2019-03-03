import random

print('Hello')

num_guesses = 0
our_number = random.randint(1, 20)

print('our_number:', our_number)

while True:
	user_guess = input('enter your guess >')
	if user_guess == 'q':
		break
	try:
		user_guess = int(user_guess)
	except ValueError as err:
		print('Not a number!!')
		print('Error:', err)
		continue
	finally:
		print('here anyway')
	num_guesses = num_guesses + 1
	
	if user_guess == our_number:
		print('Well done. You took' , num_guesses, 'guesses.')
		break
	else:
		print('Wrong guess!')
		if user_guess < our_number:
			print('my number is higher than', user_guess)
		else:
			print('my number is lower than', user_guess)
		
	

print('Done')

