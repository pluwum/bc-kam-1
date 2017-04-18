def fizz_buzz(number):
	numberTypes = (int, float, long)

	if isinstance(number, numberTypes):
		if(number % 5 == 0) and (number % 3 == 0):
			return 'FizzBuzz'
		elif(number % 3 == 0):
			return 'Fizz'
		elif(number % 5 == 0):
			return 'Buzz'	
		else:
			return number	
	else:
		raise TypeError

#mic check 1,2,3
#print(fizz_buzz(15))