#!/usr/bin/python3

import sys
import re

if len(sys.argv) != 2:
    print ("Wrong usage")
    sys.exit(1)

if re.match('.*?@tomswift ECE4564-Team01.*?', sys.argv[1]):
    fields = sys.argv[1].split('_')
    if re.match('^[12]?[0-9]?[0-9]\.[12]?[0-9]?[0-9]\.[12]?[0-9]?[0-9]\.[12]?[0-9]?[0-9]:[1-6]?[0-9]?[0-9]?[0-9]?[0-9]$', fields[1]):
        print("{}".format(fields[2]))
