#!/usr/bin/python

import re
import sys

if len(sys.argv) > 1:
    for logfile in sys.argv[1:]:
        with open(logfile, 'r') as content:
            for line in content:
                #first regex rule, look for the string "exception"
                matched = re.search('(.*exception)',line,re.I)
                if matched:
                    print matched.group()
                #add more rules, what are we looking for exactly
                #can add more if statements for filters in the beginning if we know what language or platform we're dealing with.
else:
    print "Not enough arguments"
    sys.exit()
