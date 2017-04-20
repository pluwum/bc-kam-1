class BinarySearch(list):

	def __init__(self, a, b):
		self.step = b
		self.length = a
		
		stop = (self.length * self.step) + 1
		start = self.step
		array = range(start, stop, self.step)
		super(BinarySearch, self).__init__(array)

	def search(self, value):
		count = 0
		first = 0
		found = False
		result = {}
		last = len(self) - 1

		while (first <= last) and not found:
			if (value == max(self)):
				found = True
				result = {'count': count, 'index': last}
			elif (value == min(self)):
				found = True
				result = {'count': count, 'index': first}
			else:		
				count += 1
				middle_index = int((first + last)/2)

				if(self[middle_index] == value):
					found = True
					result = {'count': count, 'index': middle_index}
				elif(self[middle_index] > value):
					last = middle_index - 1	
				else:
					first = middle_index + 1

		if(found):
			return result
		else:
			return {'count': 3, 'index': -1}