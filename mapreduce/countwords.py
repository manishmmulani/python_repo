import glob

text_files = glob.glob('docs/*.txt')

def file_contents(file_name):
	f = open(file_name, 'r')
	try :
		return f.read()
	finally:
		f.close()

source = dict((file_name, file_contents(file_name)) for file_name in text_files)

#print file_contents('countwords.py')
