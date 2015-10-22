def assort(counts):
	"""prec:  counts is a dictionary whose keys are words
and whose values are positive integers.
postc:  return a dictionary whose keys are integers
and whose values are lists containing all words paired
with the integers, sorted alphbeticallly.  Here is an example
d = {"cat":3, "dog":1, "pig":1, "horse":3, "lemur":4}
assort(d) -> {1: ["dog", "pig"], 3:["cat", "dog"], 4:["lemur"]}
"""
	assorted = {}
	
	keylist = list(counts.keys())
	for key in keylist:
		assorted[counts[key]] = []
	for key in keylist:
		assorted[counts[key]].append(key)
		#assorted[counts[key]].sort()
	return assorted
