#!/usr/bin/env python
import sys, os

def getWords(files, length):
	'''Returns a list of words equal in size to length: Args:
	- files: list of files (list)
	- length: length of words (int)
	Returns:
	- list: requested list of words'''

	# load dictionaries
	tempList = []
	for file in files:
		try:
			fh = open(file)
			for line in fh:
				tempList.append(line.strip())
			fh.close()
			print 'Loaded %s dictionary.' % (file)
		except IOError:
			print 'Could not open file %s' % file
			pass

	# remove duplicates
	tempList = list(set(tempList))

	# get words of x length
	sizedList = []
	for word in tempList:
		if len(word) == length:
			sizedList.append(word)

	# sort list and return
	sizedList.sort()
	return sizedList

def contains(word, letters):
	'''Checks to see if word contains given letters. Args:
	- word: string
	- letters: list
	Returns:
	boolean'''

	wletters = list(word)
	for wletter in wletters:
		if wletter not in letters:
			return False
		# don't count words with duplicate letters that we can't use
		if wletters.count(wletter) > letters.count(wletter):
			return False
	return True

def getCandidates(words, letters):
	'''Returns a list of words that contain given letters. Args:
	- words: list of words (list)
	- letters: list of letters (list)
	Returns:
	- list: list of words containing given letters.'''

	newList = []
	for word in words:
		if contains(word, letters):
			newList.append(word)
	return newList

def main(letters, length):
	letters = list(letters)
	print 'Letters: %s' % (', '.join(letters))
	print 'Word length: %d' % (length)

	files = os.listdir('.')
	dictionaries = []
	for i in files:
		if i.startswith('dict'):
			dictionaries.append(i)

	wordList = getWords(dictionaries, length)
	if len(wordList) == 0:
		print 'Sorry, no matches. Try a different dictionary.'
		sys.exit(-1)

	print 'There are %s %d letter words.' % ("{:,d}".format(len(wordList)), length)

	print 'Narrowing results...'
	candidates = getCandidates(wordList, letters)		

	if len(candidates) == 0:
		print 'Sorry, no matches. Try a different dictionary.'
		sys.exit(-1)

	print 'There are %s possible words:\n' % len(candidates)

	print ', '.join(candidates)

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print 'Usage: python run.py [letters] [word length]'
		sys.exit(-1)
	if not sys.argv[1].isalpha():
		print 'Only letters allowed.'
		sys.exit(-1)
	if len(sys.argv[1]) != 12:
		print '10 letters are required, given %s.' % (len(sys.argv[1]))
		sys.exit(-1)
	if not sys.argv[2].isdigit():
		print 'Not a valid length.'
		sys.exit(-1)
	main(sys.argv[1], int(sys.argv[2]))
