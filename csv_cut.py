#!/usr/bin/env python3

import csv
import sys

# The second command line argument is the file to parse
with open(sys.argv[2], newline='') as csvfile:
    for row in csv.reader(csvfile):
        # The first command line argument is the column to print
        print(row[int(sys.argv[1]) - 1])
