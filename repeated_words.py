#!/usr/local/bin/python3

#todo
#clean up exceptions
#add flag for common words


from sys import exit
from sys import argv
from collections import Counter
import string

script, filename = argv

if filename == '-h':
	print("""
	This program will analyze a text file for repeated words. 
	The 25 most common per Wikipedia are ignored. Results are printed 
	in descending order by number used. 
	Usage: command <textfile to be analyzed>""")
	exit(0)
	
	
f = open(filename, 'r')

input_text = f.read()
ignore = ['the', 'but', 'they', 'this', 'so', 'a', 'the', 'is', 'of', 'and', 'to', 'that', 'in', 'on', 'you', 'for', 'as', 'are', 'i', 'with', 'it', 'was', 'be', 'at', 'or', 'not', 'an', 'all', 'if']
ignored = 0
single_words = 0
ignore_flag = True
word_list = {}
input_text = (''.join(ch.lower() for ch in input_text if ch not in set(string.punctuation))).rstrip().lstrip().split(' ')

for word in input_text:
	if word in ignore and ignore_flag:
		ignored += 1
	elif word in word_list:
		word_list[word] += 1
	else:
		word_list[word] = 1
		
for value in sorted(word_list, key = word_list.get, reverse = False):
	if word_list[value] == 1 and len(word_list) > 100:
		single_words += 1
	else:
		print(value, '=>', word_list[value])

print()
print(len(input_text), " words were entered.")
print(len(word_list), " words are unique.")
if ignored > 0:
	print(ignored, " common words were ignored.")
if single_words > 0:
	print(single_words, " words used only once were not printed.\n")
	
f.close()
exit(0)

#common = Counter(word_list)
#common_list = common.most_common()
	
#for x in common_list:
#	print("%s => %d" % x)