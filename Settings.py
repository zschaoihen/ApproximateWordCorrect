class Settings(object):

	def __init__(self, useLD = False, useNgram = False, useDLD = False, useHybrid = False):
		self.useLD = useLD
		self.useDLD = useDLD
		self.useHybrid = useHybrid
		self.useNgram = useNgram
		self.preMode = True
		self.accMode = True
		self.minCandidate = 0
		self.maxCandidate = 0
		self.sumCandidate = 0
		self.accMatch = 0
		self.preMatch = 0

	def setMode(self, mode):
		if mode == 'precision':
			self.accMode = False
		elif mode == 'accuracy':
			self.preMode = False
		elif mode == 'both':
			pass
		else:
			raise ValueError('wrong mode parameter')

	def setLen(self, len):
		self.minCandidate = len