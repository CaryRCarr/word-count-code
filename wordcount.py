#!/usr/bin/env python

import sys
import re

def main(argv):
	"""If only a True/False statement and a file path are passed in, then the program will return the top-three words from the given file. If a key word is passed in along with the True/False statement and file path, then the number of times that the key word appears in the file will be returned."""
	if len(sys.argv) == 3 :
		#Returns the top-three if there are only three arguments.
		top_three = True
		lower_casing = sys.argv[1]
		input_path = sys.argv[2]
	if len(sys.argv) == 4 :
		#Returns the count of the number of times the key word appears if there are four arguments.
		top_three = False
		lower_casing = sys.argv[1]
		input_path = sys.argv[2]
		key_word = sys.argv[3]
	import_file = open(input_path,"r",encoding='utf-8')
	word_count = {}
	removelist = "-"
	pattern = re.compile(r'[^\w'+removelist+']')
	for x in import_file :
		word_list = x.split()
		for y in word_list :
			substitute = re.sub(pattern, '',y)
			if lower_casing :
				word = substitute.lower()
			else :
				word = substitute
			if word in word_count :
				word_count[word] = word_count.get(word) + 1
			else :
				word_count[word] = 1
	import_file.close()
	if top_three :
		newA = sorted(word_count, key=word_count.get, reverse=True)[:3]
		print("The top three words in this file are '"+newA[0]+"', '"+newA[1]+"', and '"+newA[2]+"'.")
	else :
		if lower_casing :
			key_word = key_word.lower()
		num_words = str(word_count.get(key_word))
		print("The word '"+key_word+"' appears a total of "+num_words+" time(s) in the file.")

if __name__ == "__main__":
	main(sys.argv)
