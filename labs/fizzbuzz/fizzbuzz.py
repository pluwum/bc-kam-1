def fizz_buzz(number):
	numberTypes = (int,float,long)

	if isinstance(number, numberTypes):
		if(number % 5 == 0) and (number % 3 == 0):
			return 'fizzbuzz'
		elif(number % 3 == 0):
			return 'fizz'
		elif(number % 5 == 0):
			return 'buzz'	
		else:
			return number	
	else:
		raise TypeError

#print(fizz_buzz(15))