#!/usr/bin/env python
#
# Walk through general log file and deletes line we do not need
#
# Author: Erik
# Last changed & version:
#
# Todos:
# * Optional log file name, default is messages

# Imports
import sys
import os
import os.path
from datetime import datetime

# Global variables
__author__ = 'Erik'
__version__ = 'v1'
__last_changed__ = '2015-00-19'

to_delete = []

path = sys.argv[0].split('\\')
name = path[len(path)-1]
print(path)

exit()

# Compute longest string to delete. Just used for a statistical output at the end
max_length = 0
for key in to_delete:
    if len(key) > max_length: max_length = len(key)

print("Starting {0:} {1:}".format(sys.argv[0], version))
print("Deleting lines from file 'message' containing the following strings:")
print(to_delete)

try:
    messages = open("messages")
except:
    print("messages file does not exist ()")
    exit()

# Constructing output file name
time1 = str(datetime.now())
time2 = time1.replace(" ", "_")
time = time2.replace(":", "-")
filename = "messages_reduced-{}.txt".format(time)

if not os.path.exists(filename):
    print("\nOutfile ", filename)
    oldstdout = sys.stdout
    sys.stdout = open(filename, "a")
else:
    print("\nOutfile {} exists! Script will terminate", format(filename))
    exit()

# Crreate dict to count deleted lines
# for word in to_delete:
#  count[word] = 0

count = dict()
linenr = 0
deletenr = 0
for line in messages:
    linenr += 1
    bool = True
    for word in to_delete:
        if word in line:
            count[word] = count.get(word, 0) + 1
            deletenr += 1
            bool = False
            break
    if bool: print(line.rstrip())

# Restore original stdout
sys.stdout = oldstdout

print("Deleted {0:} out of {1:} lines with the following strings:".format(deletenr, linenr))
max_value = 0
for key, value in count.items():
    if len(str(value)) > max_value: max_value = len(str(value))

format1 = "{0:" + str(max_length) + "s} {1:" + str(max_value) + "d}".rstrip()
for key, value in count.items():
    print(format1.format(key, value))
