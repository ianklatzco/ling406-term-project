# for every file in this directory
    # if we have > 5 lines between two empty lines
        # remove a block of text between two newlines
    # if we have 1 line between two empty lines
        # remove that line and one empty line

import os
import json

for f in os.listdir():
    biglist = []
    arr = []
    for line in open(f) :
        if line != "\n":
            arr.append( line )
        else:
            biglist.append(arr)
            arr = []

    for x in biglist:
        print(len(x))

    for x in biglist:
        if len(x) > 5 or len(x) == 1:
            biglist.remove(x)

    f = open(f+"fmtd",'w')

    json.dump(biglist,f)


        # iterate over list until newline
        # add to new list
        # count length of that list
        # make decision based on above rules

