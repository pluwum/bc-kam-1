def data_type(arg):

	if isinstance(arg, str):
		return len(arg)
	elif isinstance(arg, bool):
		return arg
	elif arg is None:
		return "no value"	
	elif isinstance(arg, int):
		if arg > 100:
			return "More than 100"
		elif arg < 100 :
			return "Less than 100"
		else:
			return "equal to 100"
	elif isinstance(arg, list):
		if(len(arg)) > 2:
			return arg[2]
		else:
			return None