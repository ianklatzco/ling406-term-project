import os
import json

totalcount = []
for filename in os.listdir():
    arr = []
    if ".txtfmtd" in filename:
        # open file
        f = open(filename,'r')
        content = json.load(f)
        for thing in content:
            # print(thing[4][3:])
            try:
                for idx in range(0,4):
                    if thing[4][3:-1] in thing[idx]:
                        arr.append(thing[idx][2:6])
            except:
                pass
        # print(arr.count('naiv'))
        # print(arr.count('mine'))
        # print(arr.count('kify'))
        # print(arr.count('real'))
        if len(arr) >= 50:
            print("player: "+filename)
            print( arr.count('real') / len(arr) ) 


