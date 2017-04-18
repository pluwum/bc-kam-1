"""
        Counts the occurrences or characters in a word
"""

def words(word):
	words = word.split()
	count = {}
	for partial in words:
		if partial.isdigit():
			count[int(partial)] = words.count(partial)
		else:	
			count[partial] = words.count(partial)
	return count