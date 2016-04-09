import random

class MarkovState:
	def __init__(self, state):
		self.state = state
		self.follow = {}
		self.total = 0
	def __hash__(self):
		return __hash__(self.state)
	def __eq__(self, another):
		return hasattr(another, 'state') and self.state = another.state

	def is_matching(self, other):
		return self.state == other

	def append(self, word):
		if word in self.follow:
			self.follow[word] += 1
		else:
			self.follow[word] = 1
		self.total += 1

	def generate_next(self):
		goal = random.randint(0, self.total)

		for key, value in self.follow.items():
			goal -= value
			if goal <= 0:
				return key