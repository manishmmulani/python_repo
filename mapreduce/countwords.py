import glob

text_files = glob.glob('docs/*.txt')

def file_contents(file_name):
	f = open(file_name, 'r')
	try :
		return f.read()
	finally:
		f.close()

source = dict((file_name, file_contents(file_name)) for file_name in text_files)

def parse(content):
	for line in content.splitlines():
		for word in line.split():
			yield word

for key in source:
	print "Parsing file " + key
	for word in parse(source[key]):
		print word

#print file_contents('countwords.py')
