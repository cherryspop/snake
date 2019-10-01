#!/usr/bin/env python3
from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']
coll = []

with open(argv[1], 'r') as f, open(argv[2], 'w') as c:
  for line in f:
    for word in ignore:
      if word in line:
        line = '!\n'
        continue
    if line == '!\n':
      continue
    c.write(line)