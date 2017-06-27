# purely an aside. don't look at this file.
# counts the number of messages sent by each user in our groupchat.
# results in out.txt.

import json

d = {}

with open("../output/json/"+'xFF5353.jsonl') as data_file:    
    for line in data_file.readlines():
        message_json = json.loads(line)
        key = message_json['from']['print_name']
        if key in d:
            d[key] += 1
        else:
            d[key] = 1
#print ( d )

import operator
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print(sorted_d)

