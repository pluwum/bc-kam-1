def find_max_min(alist):
	maxi = max(alist)
	mini = min(alist)

	if maxi == mini:
		return [maxi]
	else:	
		return [mini, maxi]
