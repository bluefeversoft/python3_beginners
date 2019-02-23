print('welcome')

user_in = input('enter a palindrome of at least 5 letters >')

user_in_length = len(user_in)
pal = user_in[::-1]

print('your word was', user_in)
print('you entered', user_in_length, 'letters')

if user_in_length < 5:
	print('Not enough letters in that!')
elif pal == user_in:
	print('Cool!', user_in, 'is indeed a palindrome')
else:
	print("Sorry, that's not a palindrome :(")

print('Thanks for playing!')






