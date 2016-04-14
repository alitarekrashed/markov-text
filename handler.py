from markov import *
import json
import glob

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

def twitter_archive(filename):
	allFiles = glob.glob(filename + '/data/js/tweets/*.js')
	tweets_decoded = []
	for month in allFiles:
		tweet_file = open(month)
		stringFile = "".join(tweet_file.readlines()[1:])
		temp = json.loads(stringFile)
		for tweet in temp:
			tweets_decoded.append(tweet['text'])

	m = MarkovEngine()	
	f = open('output.txt', 'w')
	for tweet in tweets_decoded:
		t = tweet.split(' ')
		for x in range(0, len(t) - 2):
			m.append_instance((t[x], t[x+1]), t[x+2])

	print(m.generate_chain(140))
