import os
import json

totalcount = []
for filename in os.listdir():
    if ".txtfmtd" in filename:
        # open file
        f = open(filename,'r')
        content = json.load(f)
        for thing in content:
            # print(thing[4][3:])
            try:
                for idx in range(0,4):
                    if thing[4][3:-1] in thing[idx]:
                        totalcount.append(thing[idx][2:6])
            except:
                pass
        # iterate thru each line

print(totalcount.count('naiv'))
print(totalcount.count('mine'))
print(totalcount.count('kify'))
print(totalcount.count('real'))
