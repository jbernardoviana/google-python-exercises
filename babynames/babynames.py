#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import pdb

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def get_info(tagname, html):
  matches = re.findall('<{}.*?>(.+?)</{}>'.format(tagname, tagname), html)
  # [1, 'Joao', 'Joana', 2, 'Tomas', 'Rita', ...]

  ranks = matches[::3][0:-1]
  # [1,2,3,..]
  male_names = matches[1::3]
  female_names = matches[2::3]

  results = []
  for ix,rank in enumerate(ranks):
    #if ix == 999 : pdb.set_trace()
    results.append({'rank': rank, 'male': male_names[ix], 'female': female_names[ix]})
  return results

def print_names(data):
  print('Male  Female  Rank')
  for dict in sorted(data, key=lambda d: d['male']):
    print('{} {} {}'.format(dict['male'], dict['female'], dict['rank']))
  return

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  f = open(filename, 'rU')
  parsed_html = f.read() # load it all to memory
  f.close()

  data = get_info('td', parsed_html)
  #pdb.set_trace()
  # data => [ .., {'male': 'Sonny', 'female': 'Delilah', 'rank': '878'}, {'male': 'Auston', 'female': 'Jena', 'rank': '879'}, .. ]

  year_match = re.search('Popularity\sin\s(\d\d\d\d)', parsed_html)
  if not year_match:
    # We didn't find a year, so we'll exit with an error message.
    sys.stderr.write('Couldn\'t find the year!\n')
    sys.exit(1)
  year = year_match.group(1)
  print('\n' + year)

  print_names(data)

  # return ['2002', 1, 'Joao', 'Rita', '2', ...]
  names = list(map(lambda e: e.values(), data))
  # names => ['2002', [ 1, 'Joao', 'Rita'], ['2', ..], ..]
  flattened_names = [y for x in names for y in x]

  return [year] + flattened_names

# -- USAGE ----

# python2 babynames/babynames.py babynames/baby1998.html babynames/baby2002.html
# => it will print the data parsed
#
# python2 babynames/babynames.py --summarfile babynames/baby1998.html babynames/baby2002.html
# => it will extract the data to files .txt

# -------------------------------------------------------------------------------------------


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # passing multiple .html files
  if len(args) >= 1:
    for filename in args:
      names = extract_names(filename)
      # Make text out of the whole list
      text = '\n'.join(names)

      if summary:
        print('extracting to file ...')
        outf = open(filename + '.summary', 'w')
        outf.write(text + '\n')
        outf.close()
      else:
        #print text

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

if __name__ == '__main__':
  main()
