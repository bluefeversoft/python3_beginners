# calculator
print('Welcome to this calcuator!')
input('press Enter to continue..')

num_one_text = input('Enter the first number:')
num_two_text = input('Enter the second number:')

print(type(num_one_text))
print(type(num_two_text))

num_one = int(num_one_text)
num_two = int(num_two_text)

input('press enter to run calculation...')

print(type(num_one))
print(type(num_one))

num_mult = num_one * num_two
num_div = num_one / num_two
num_add = num_one + num_two
num_subtract = num_one - num_two
num_mod = num_one % num_two
num_floordiv = num_one // num_two

print (str(num_one) + ' * ' + str(num_two) + ' = ' + str(num_mult))
print (str(num_one) + ' / ' + str(num_two) + ' = ' + str(num_div))
print (str(num_one) + ' + ' + str(num_two) + ' = ' + str(num_add))
print (str(num_one) + ' - ' + str(num_two) + ' = ' + str(num_subtract))
print (str(num_one) + ' % ' + str(num_two) + ' = ' + str(num_mod))
print (str(num_one) + ' // ' + str(num_two) + ' = ' + str(num_floordiv))
print('Done!')

























