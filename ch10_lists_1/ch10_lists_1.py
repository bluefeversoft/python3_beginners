
shopping_list = []

while True:
	user_input = input('Enter an item for your shopping list>')
	if user_input == 'q':
		break
	else:
		shopping_list.append(user_input)

print('your final shopping list:' , shopping_list)

for item in shopping_list:
	print(item)
	