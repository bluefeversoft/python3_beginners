convert = input('What should I convert to? (F or C) >')
temp_str = input('What temperature? >')

temp_f = float(temp_str)

if convert == 'C':
	result = (temp_f - 32) * (5 / 9)
	result = round(result)
	print(int(temp_f), 'in Celsius is', result)
elif convert == 'F':
	result = (temp_f * (9 / 5)) + 32
	result = round(result)
	print(int(temp_f), 'in Fahrenheit is', result)
else:
	print('Did not understand the input')
	
print('Thanks for using this program')





