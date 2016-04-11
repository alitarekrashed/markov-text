import random

class MarkovState:
	def __init__(self, state): #note, one element tuple being treated as a string, maybe a problem?, could just require size > 1
		self.state = state
		self.follow = {}
		self.total = 0
	def __hash__(self):
		return hash(self.state)
	def __eq__(self, another):
		return hasattr(another, 'state') and self.state == another.state
	def __str__(self):
		result = ""
		for x in range(0, len(self.state)):
			result += self.state[x]
			if(x < len(self.state) - 1):
				result += " "
		return result

	def is_matching(self, other):
		return self.state == other

	def append(self, word):
		if word in self.follow:
			self.follow[word] += 1
		else:
			self.follow[word] = 1
		self.total += 1

	def generate_next(self):
		if self.total == 0:
			return None

		goal = random.randint(0, self.total)

		for key, value in self.follow.items():
			goal -= value
			if goal <= 0:
				return key

	def adjust_state(self, new):
		adjusted = []
		for x in range(1, len(self.state)):
			adjusted.append(self.state[x])
		adjusted.append(new)

		return MarkovState(tuple(adjusted))


class MarkovEngine:
	def __init__(self):
		self.states = []

	def append_instance(self, state, next):
		found = False
		target = MarkovState(state)
		for s in self.states:
			if s == target:
				found = True
				s.append(next)

		if not found:
			target.append(next)
			self.states.append(target)

	def exists(self, state):
		target = MarkovState(state)
		for s in self.states:
			if s == target:
				return True
		else:
			return False

	def get_state(self, to_match):
		for s in self.states:
			if s == to_match:
				return s
		return None

	def get_random_state(self):
		index = random.randint(0, len(self.states) - 1)
		return self.states[index]

	def generate_chain(self, length):
		result = ""
		current = self.get_random_state()
		result += str(current)
		total_length = len(result)

		while total_length < length:
			next = current.generate_next()

			if next != None:
				total_length += len(next) + 1
				if total_length <= length:
					result += " " + next
					tmp = current.adjust_state(next)
					current = self.get_state(tmp)
			
			if next == None or current == None:
				total_length = length

		return result



