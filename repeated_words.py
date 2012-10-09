#!/usr/local/bin/python3

#todo
#clean up exceptions
#add flag for common words

#	Reads a text file line by line. Adds the words to a dictionary as found
#	and updates the count as found again.
#	Punctuation and whitespace are stripped out, words are turned
#	lowercase.
#	Common words are ignored.
#	Words are printed out with the total count starting at the
#	lowest number.

from sys import exit
from sys import argv
from collections import Counter
import string
import os

script, *filename = argv

help = """
This program will analyze a text file for repeated words.
The 25 most common per Wikipedia are ignored. Results are printed
in descending order by number used. Anytime more then 100 unique
words are found words found once are not displayed.
Usage: command <textfile to be analyzed>"""


print(os.path.isfile(str(filename[0])))

if not os.path.isfile(str(filename[0])):
    print(help)
    exit(0)


ignore = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i',
          'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at',
          'this', 'but', 'his', 'by', 'from']

words = 0
ignored = 0
single_words = 0
word_list = {}


for line in open(filename[0]):
    input_text = ((''.join(ch.lower() for ch in line if ch not in
                       set(string.punctuation))).rstrip().lstrip().split(' '))
    for word in input_text:
        words += 1
        if word in ignore:
            ignored += 1
        elif word in word_list:
            word_list[word] += 1
        else:
            word_list[word] = 1


for value in sorted(word_list, key=word_list.get, reverse=False):
    if word_list[value] == 1 and len(word_list) > 100:
        single_words += 1
    else:
        print(value, '=>', word_list[value])


print()
print(words, " words were entered.")
print(len(word_list), " words are unique.")
if ignored:
    print(ignored, " common words were ignored.")
if single_words:
    print(single_words, " words used only once were not printed.\n")

exit(0)

#common = Counter(word_list)
#common_list = common.most_common()
#for x in common_list:
#	print("%s => %d" % x)
