class Calculate(object):

	def __init__(self, dict, function):
		self.function = function
		self.dict = {}
		for entry in dict:
			self.dict.setdefault(entry,len(entry))

	#Optimiztion for GED. If the length difference between the headword and a entry 
	#if over 4, then we just simply throw this entry away.
	def _filter(self, word, entry):
		if abs(len(word) - len(entry)) >= 4:
			return False
		else:
			return True

	def getCandidate(self, word):
		if word in self.dict:
			return [word]
		return self.calcu(word)

	def calcu(self, word):
		minDistance = len(word)
		candidate = []
		for entry, lens in self.dict.items():
			if self._filter(word, entry):
				temp = self.function(word, entry)
				if temp < minDistance:
					minDistance = temp
					candidate.clear()
					candidate.append(entry)
				elif temp == minDistance:
					candidate.append(entry)
		return candidate