#!/usr/bin/env python
import sys

def getWords(files, length):
	'''Returns a list of words equal in size to length: Args:
	- files: list of files (list)
	- length: length of words (int)
	Returns:
	- list: requested list of words'''

	list = []
	for file in files:
		fh = open(file)
		for line in fh:
			list.append(line.strip())
		fh.close()

	sizedList = []
	for word in list:
		if len(word) == length:
			sizedList.append(word)

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

	wordList = getWords(['wordlist.txt'], length)
	print 'There are %s %d letter words.' % ("{:,d}".format(len(wordList)), length)

	print 'Narrowing results...'
	candidates = getCandidates(wordList, letters)		

	print 'There are %s possible words:\n' % len(candidates)

	print ', '.join(candidates)

if __name__ == '__main__':
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
