"""
Uses Map Reduce programming paradigm to compute how many times each 'title term' occurs across titles
for every author.

We use 'mincemeat.py' map reduce library for this purpose.

Input files are present in hw3data directory
"""

import re
import glob
import mincemeat

text_files = glob.glob("hw3data/*")
#text_files = glob.glob("hw3data/c0001")

def file_contents(file):
	f = open(file, 'r')
	try:
		return f.read()
	finally:
		f.close()

def mapfn(key, value):
	import terms.TermExtractor as termExt
	def parse_line(line):
		record_arr = line.split(":::")
		length = len(record_arr)
		if length == 3:
			authors = record_arr[1].split("::")
			title = record_arr[2]
			return (authors, termExt.extract(title))
		else:
			print "Error parsing line : " + line

	for line in value.splitlines():
		parsedOutput = parse_line(line)
		if parsedOutput != None:
			authors, terms = parsedOutput
			for author in authors:
				for term in terms:
					#print author, term
					yield author, term

def reducefn(key, value):
	termCountMap = {}
#	print key, value
	for term in value:
		if term not in termCountMap:
			termCountMap[term] = 1
		else:
			termCountMap[term] += 1
	return termCountMap

s = mincemeat.Server()

s.datasource = dict((file, file_contents(file)) for file in text_files)
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="abc")
#print results

f = open("output.txt", "w+")
for key in results:
	arr = []
	for term in results[key]:
		#term : count
		arr.append(term + ":" + str(results[key][term]))
	arr = sorted(arr, key = lambda x: int(x.split(":")[1]), reverse=True)

	line = key + ","
	for item in arr:
		line += item + ","

	f.write(line + "\n")

