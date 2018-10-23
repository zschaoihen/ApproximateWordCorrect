import time
import os, sys, getopt
import jellyfish
from check import writeCheck
from ngram import NGram
from output import Output
from calcu import Calculate
from Settings import Settings

#Record starting time.
start = time.time()

#Create a Setting object to record parameters.
setting = Settings()

#This part is the command line parameter parser. You can choose 4 mode, global(LD), 
#DLD, ngram and a hybrid mode(not use in this report).
shortargs = 'f:hgn:m:de'
longargs = ['filepath=', 'help', 'global', 'ngram=', 'mode=', 'dld', 'enhance']
try:
	opts, args = getopt.getopt(sys.argv[1:], shortargs, longargs)
except getopt.GetoptError:
    print('should use kt.py -f <datafolder> -g/-d/-n/-e')
    sys.exit(2)
for opt, arg in opts:
	if opt in ('-h', '--help'):
		print ('kt.py -f <datafolder> -g/-d/-n/-e')
		sys.exit()
	elif opt in ('-f', '--filepath'):
		fpath = arg
	elif opt in ('-g', '--global'):
		setting.useLD = True
	elif opt in ('-d', '--dld'):
		setting.useDLD = True
	elif opt in ('-n', '--ngram'):
		setting.useNgram = True
		n = int(arg,10)
	#Determine the output for different evaluation metrics.
	elif opt in ('-m', '--mode'):
		try:
			setting.setMode(arg.lower())
		except ValueError as e:
			print(e)
			sys.exit()
	elif opt in ('-e', '--enhance'):
		setting.useHybrid = True

#Open and read the dataset.
with open(fpath + '/data/misspell.txt', 'r') as tokenList:
	tokens = [line.strip() for line in tokenList.readlines()]

with open(fpath + '/data/dictionary.txt', 'r') as dictionary:
	dictionaryList = tuple([line.strip() for line in dictionary.readlines()])

with open(fpath + '/data/correct.txt', 'r') as correct:
	correctList = [line.strip() for line in correct.readlines()]

setting.setLen(len(tokens))

#Create log.
dirPath = fpath + '/Log'
if not os.path.exists(dirPath):
	os.mkdir(dirPath)

if not os.path.exists(dirPath + '/checkCorrect.txt'):
	with open(dirPath + '/checkCorrect.txt', 'w') as check:
		writeCheck(check, correctList, dictionaryList)

if setting.useLD:
	calcu = Calculate(dictionaryList, jellyfish.levenshtein_distance)
	logName = 'LD'
elif setting.useDLD:
	calcu = Calculate(dictionaryList, jellyfish.damerau_levenshtein_distance)
	logName = 'DLD'
elif setting.useNgram:
	calcu = NGram(dictionaryList, n)
	logName = 'NGram(n={})'.format(n)
elif setting.useHybrid:
	calcu = Calculate(dictionaryList, jellyfish.damerau_levenshtein_distance)
	logName = 'Hybrid'
output = Output(logName, dirPath, calcu, setting, tokens, correctList)
output.getOutput()

#Calculate and print the runtime.
end = time.time()
print('run time: %.3fs' % (end - start))

output.runtime(end-start)
output.closeLog()