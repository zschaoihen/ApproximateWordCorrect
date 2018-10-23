import sys
import random
from ngram import NGram

class Output(object):

	#Take the dataset, save the dictionary in python dict structure.
	def __init__(self, logName, logPath, func, setting, tokens = [], correctList = []):
		self.func = func
		self.tokens = tokens
		self.correctList = correctList
		self.setting = setting
		self._createLog(logPath, logName)
		

	def _createLog(self, logPath, logName):
		if self.setting.accMode:
			self.acclog = open(logPath + '/' + logName + '_Accuracy.txt', 'w')
		if self.setting.preMode:
			self.prelog = open(logPath + '/' + logName + '_Precision.txt', 'w')

	#Close log to prevent data loss.
	def closeLog(self):
		if self.setting.accMode:
			self.acclog.close()
		if self.setting.preMode:
			self.prelog.close()

	def getOutput(self):
		for index in range(len(self.tokens)):
			#First we get the candidate list for each headword.
			candidate = self.func.getCandidate(self.tokens[index])
			if self.setting.useHybrid:
				ngram = NGram(candidate)
				candidate = ngram.getCandidate(self.tokens[index])
			#Then we update precision(accuracy) match number base on candidate list.
			if self.setting.accMode:
				self.acclog.write('{},{}\n----------\n'.format(index, self.tokens[index]))
				self._calcuAcc(candidate, index)
			if self.setting.preMode:
				self.prelog.write('{},{}\n----------\n'.format(index, self.tokens[index]))
				self._calcuPre(candidate, index)
		try:
			if self.setting.accMode:
				self._getAcc(len(self.correctList))
			if self.setting.preMode:
				self._getPre(len(self.correctList))
		except:
			print('correct file is empty')
			sys.exit()

	def _calcuAcc(self, candidate, index):
		if len(candidate) > 1:
			temp = candidate[random.randint(0, len(candidate) - 1)]
		else:
			temp = candidate[0]

		self.acclog.write('{}'.format(temp))
		if self.correctList[index] == temp:
			self.setting.accMatch = self.setting.accMatch + 1
			self.acclog.write('   *')
		self.acclog.write('\n')
		self.acclog.write('{}\n\n'.format(self.correctList[index]))

	def _calcuPre(self, candidate, index):
		if len(candidate) < self.setting.minCandidate:
			self.setting.minCandidate = len(candidate)
		if len(candidate) > self.setting.maxCandidate:
			self.setting.maxCandidate = len(candidate)
		self.setting.sumCandidate = self.setting.sumCandidate + len(candidate)
		for candi in candidate:
			self.prelog.write('{}'.format(candi))
			if self.correctList[index] == candi:
				self.setting.preMatch = self.setting.preMatch + 1
				self.prelog.write('   *')
			self.prelog.write('\n')
		self.prelog.write('{}\n\n'.format(self.correctList[index]))

	#Print accuracy.
	def _getAcc(self, lens):
		print('Accuracy: %.2f%%' % (self.setting.accMatch / lens* 100))
		self.acclog.write('Accuracy: %.2f%%\n' % (self.setting.accMatch / lens* 100))

	#Print precision, recall and candidate number.
	def _getPre(self, lens):
		print('Precision: %.2f%%' % (self.setting.preMatch / self.setting.sumCandidate * 100))
		print('Recall: %.2f%%' % (self.setting.preMatch / lens * 100))
		print('Max candidate number: %d' % self.setting.maxCandidate)
		print('Min candidate number: %d' % self.setting.minCandidate)
		print('Average candidate number: %.2f' % (self.setting.sumCandidate / lens))
		self.prelog.write('Precision: %.2f%%\n' % (self.setting.preMatch / self.setting.sumCandidate * 100))
		self.prelog.write('Recall: %.2f%%\n' % (self.setting.preMatch / lens * 100))
		self.prelog.write('Max candidate number: %d\n' % self.setting.maxCandidate)
		self.prelog.write('Min candidate number: %d\n' % self.setting.minCandidate)
		self.prelog.write('Average candidate number: %.2f\n' % (self.setting.sumCandidate / lens))

	def runtime(self, time):
		if self.setting.accMode:
			self.acclog.write('runtime: %.2fs\n' % time)
		if self.setting.preMode:
			self.prelog.write('runtime: %.2fs\n' % time)


