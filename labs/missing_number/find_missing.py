def find_missing(arg1, arg2):
	if isinstance(arg1, list) and isinstance(arg2, list):
		
		if len(arg1) == 0 and len(arg2) == 0:
			return 0
		elif arg1 == arg2:
			return 0
		else:
			arg1 = set(arg1)
			arg2 = set(arg2)
			diff = arg1 ^ arg2

			return diff.pop()	