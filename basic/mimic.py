#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys
import pdb


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++

  mimic_dict = {}
  # mimic_dict.setdefault("list", [])

  f = open(filename, 'r')
  text = f.read()
  f.close()
  words = list(map(lambda x: x.lower(), text.split()))

  # Pseudo
  # iterate with index
  # if its not a key of mimic_dict, add it as a list
  # if it is, append it

  # for ix,word in enumerate(words):
  #   if word not in mimic_dict:
  #     next_word = words[(ix + 1) % len(words)]
  #     mimic_dict[word] = [next_word]
  #   else:
  #     next_word = words[(ix + 1) % len(words)]
  #     mimic_dict[word].append(next_word)

  #   # or
  #   next_word = words[(ix + 1) % len(words)]
  #   mimic_dict[word] = mimic_dict.get(word, []) + [next_word]

  # return mimic_dict

  # -- OR ---
  prev = ''
  for word in words:
    if prev not in mimic_dict:
      mimic_dict[prev] = [word]
    else:
      mimic_dict[prev].append(word)
    prev = word

  return mimic_dict

  # -- OR ---
  # prev = ''
  # for word in words:
  #   mimic_dict[prev] = mimic_dict.get(prev, []) + [word]
  #   prev = word

  # return mimic_dict

def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # +++your code here+++

  if word and word in mimic_dict:
    print('{} :: {}').format(word, ', '.join(mimic_dict[word]))
  else:
    for word,next_list in mimic_dict.items():
      print('{} :: {}'.format(word, ', '.join(next_list)))


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) > 3 or len(sys.argv) < 2 :
    print 'All words usage: ./mimic.py file-to-read'
    print 'Specific word usage: ./mimic.py file-to-read word-to-check'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  if len(sys.argv) > 2:
    print_mimic(dict, sys.argv[2])
  else:
    print_mimic(dict, '')

if __name__ == '__main__':
  main()
