#print __name__  outputs terms.TermExtractor
#print __file__  outputs terms/TermExtrator.py

from __future__ import absolute_import

import re
from stopwords import allStopWords

def extract(phrase):
	list_of_words = phrase.split()

	# replace hiphens with " "
	list_of_words = map( lambda x: x.replace("-", " ") if "-" in x else x, list_of_words )

	# replace non (alpha/numeric/space) characters by null
	list_of_words = map( lambda x: re.sub(r'[^a-zA-Z0-9 ]', '', x), list_of_words )

	# ignore single letter words and stopWords
	list_of_words = filter( lambda x: len(x) > 1 and x not in allStopWords, list_of_words )

	return list_of_words

