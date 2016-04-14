import random

class MarkovEngine:
	def __init__(self):
		self.states = {}

	#adds an occurence of a state to the engine
	def append_instance(self, state, next):
		found = False
		if state in self.states:
			follow = self.states.get(state)
			follow.append(next)
		else:
			self.states[state] = [next]

	#checks to see if a state is being stored (might be unnecessary with get-state() function)
	def exists(self, state):
		return state in self.states

	#gets a random state from the states stored by the engine
	def get_random_state(self):
		index = random.randint(0, len(self.states) - 1)
		all_keys = list(self.states.keys())
		return all_keys[index]

	def next_state(self, state):
		if state in self.states:
			follow = self.states.get(state)
			index = random.randint(0, len(follow) - 1)
			return follow[index]
		else:
			return None

	def adjust_state(self, current, next):
		adjusted = []
		for x in range(1, len(current)):
			adjusted.append(current[x])
		
		adjusted.append(next)
		return tuple(adjusted)

	#takes a length for the result and returns a string
	def generate_chain(self, length, seed = None):
		if seed is None:
			current = self.get_random_state()
		else:
			current = seed

		result = ""
		for x in range(0, len(current)):
			result += current[x]
			if x < len(current) - 1:
				result += " "

		total_length = len(result)

		while total_length < length:
			next = self.next_state(current)

			if next != None:
				total_length += len(next) + 1
				if total_length <= length:
					result += " " + next
					current = self.adjust_state(current, next)
			
			if next == None or current == None:
				total_length = length

		return result



