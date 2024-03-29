#!/usr/local/bin/python3

#todo
#clean up exceptions
#add flag for common words


import string
import os
import sys

script, *filename = sys.argv

help_message = """
This program will analyze a text file for repeated words.
The 25 most common per Wikipedia are ignored. Results are printed
in descending order by number used. Anytime more then 100 unique
words are found words found once are not displayed.
Usage: command <textfile to be analyzed>"""


# stupid hack to check for valid file and ignore other input
if not filename or not os.path.isfile(str(filename[0])):
    print(help_message)
    sys.exit(0)

filename = filename[0]

ignore = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i',
          'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at',
          'this', 'but', 'his', 'by', 'from']

words = 0
ignored = 0
single_words = 0
word_list = {}


for line in open(filename):
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
        print(f"{value} => {word_list[value]}")


print(f"\n{words} were entered.")
print(f"{len(word_list)} words are unique.")
if ignored:
    print(f"{ignored} common words were ignored.")
if single_words:
    print(f"{single_words} words used only once were not printed.\n")

sys.exit(0)

