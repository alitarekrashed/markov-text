from markov import *

def text_dump(filename):
	f = open(filename, 'r')
	test = []

	for line in f:
		for word in line.split():
			test.append(word)

	print("length of corpus: " + str(len(test)))
	m = MarkovEngine()
	for x in range(0, len(test) - 2):
		m.append_instance((test[x], test[x+1]), test[x+2])

	print(m.generate_chain(200))
