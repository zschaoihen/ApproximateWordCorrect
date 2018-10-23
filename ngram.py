import random

class NGram(object):

	def __init__(self, dict, n = 2, _pad = '$'):
		self.n = n
		self._pad_str = _pad * (n-1)
		self.dict = {}
		for entry in dict:
			temp = list(self._split(self._padding(entry)))
			self.dict.setdefault(entry,{}).setdefault(len(temp), temp)

	#Pad the word with $ or any preset character.
	def _padding(self, word):
		return self._pad_str + word + self._pad_str

	#Create substring list for each word.
	def _split(self, word):
		for i in range(len(word) - self.n + 1):
			yield word[i:i + self.n]

	#Extract candidate for the dictionary.
	def getCandidate(self, word):
		if word in self.dict:
			return [word]
		wList = list(self._split(self._padding(word)))
		return self.calcu(wList)

	#Compare two list of substring and calculate the n-gram distance.
	def compare(self, xList, yList):
		minus = 0
		xList.sort()
		for x in range(len(xList)):
			if xList[x] == xList[(x+1)%len(xList)]:
				break
			else:
				for y in yList:
					if xList[x] == y:
						minus = minus + 1
						break

		return len(xList) + len(yList) - 2 * minus

	def calcu(self, wList):
		minDistance = len(wList) * 3
		candidate = []
		for entry, record in self.dict.items():
			for lens, eList in record.items():
				temp = self.compare(wList, eList)
				if temp < minDistance:
					minDistance = temp
					candidate.clear()
					candidate.append(entry)
				elif temp == minDistance:
					candidate.append(entry)
		return candidate