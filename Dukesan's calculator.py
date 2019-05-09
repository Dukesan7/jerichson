import time, os
def calc():
	fn = int(input('first number: '))
	sn = int(input('second number: '))
	print(" * / + - ")
	print(" **  to the power of ")

	mid = input(' : ')

	if mid == '*':
		print(fn * sn)

	if mid == '/':
		print(fn / sn)

	if mid == '+':
		print(fn + sn)

	if mid == '-':
		print(fn - sn)

	if mid == '**':
		print(fn ** sn)

	os.system('pause')
	os.system('cls')
	calc()

calc()
