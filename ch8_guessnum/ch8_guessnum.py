import random

num_guesses = 0
our_number = random.randint(1, 20)

#print(our_number)

while True:
	user_guess = input('enter your guess >')
	if user_guess == 'q':
		break
	user_guess = int(user_guess)
	num_guesses = num_guesses + 1
	if user_guess == our_number:
		print('correct! You took', num_guesses, 'guesses')
		break
	else:
		print('Wrong!!!')
		if user_guess < our_number:
			print('my number is higher than', user_guess)
		else:
			print('my number is lower than', user_guess)
	


print('ALL DONE')


