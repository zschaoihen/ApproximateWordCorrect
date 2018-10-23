#Check whether there is already a correct-dictionary comparision file.
#If there isn't one, create a new one.
def writeCheck(check, correctList, dictionaryList):
	for index in range(len(correctList)):
		check.write('{},{}'.format(index + 1, correctList[index]))
		try:
			dictionaryList.index(correctList[index])
		except:
			check.write('\n')
		else:
			check.write('.  *\n')