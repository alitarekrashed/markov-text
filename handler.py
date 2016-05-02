from markov import *
import json
import glob
import random

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
	start_seeds = []
	for month in allFiles:
		tweet_file = open(month)
		stringFile = "".join(tweet_file.readlines()[1:])
		temp = json.loads(stringFile)
		for tweet in temp:
			if not 'retweeted_status' in tweet:
				text = tweet['text'].split()
				filtered_text = []
				for word in text:
					if not word.startswith('@') and not word.startswith('http'):
						filtered_text.append(word)

				tweets_decoded.append(filtered_text)
				if(len(filtered_text) > 2):
					start_seeds.append((filtered_text[0], filtered_text[1]))


	m = MarkovEngine()	
	f = open('output.txt', 'w')
	for tweet in tweets_decoded:
		for x in range(0, len(tweet) - 2):
			m.append_instance((tweet[x], tweet[x+1]), tweet[x+2])

	return (m, start_seeds)
		
if __name__ == '__main__':
 	method = input("You can generate markov text chains using a twitter archive folder, or a txt file. If you would like to use a twitter archive, please enter [twitter archive], otherwise enter [text]")
 	if method == 'twitter archive':
 		filename = input("What is your twitter archive source? ")
 		engine_and_seeds = twitter_archive(filename)
 		m = engine_and_seeds[0]
 		start_seeds = engine_and_seeds[1]
 		length = int(input("What is the maximum length of the generated chains? "))
 		while True:
 			n = input('Press enter to generate a new chain, type \'stop\' to quit: ')
 			if n.lower() == 'stop':
 				break
 			print(m.generate_chain(length, start_seeds[random.randint(0, len(start_seeds) - 1)]))
 			print()
 	else:
 		filename = input("What is your text dump source? ")
 		engine = text_dump(filename)
 		length = int(input("What is the maximum length of the generated chains? "))
 		while True:
 			n = input('Press enter to generate a new chain, type \'stop\' to quit: ')
 			if n.lower() == 'stop':
 				break
 			print(engine.generate_chain(length))
 			print()

