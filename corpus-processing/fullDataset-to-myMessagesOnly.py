'''
    fullDataset-to-myMessagesOnly.py
        converts JSON-formatted datasets with a mix of messages from lots
        of people to newline-separated messages typed by me alone.
'''

import os
import json

# for each file ../output/json/USERNAME.jsonl
    # create a file in ../output/my-messages-only/USERNAME-my-messages-only.txt

# afaict jsonl just means newline-separated json
for filename in os.listdir('../output/json'):

    outfile = open('../output/my-messages-only/'+filename.replace('jsonl','txt'),'w')

    with open("../output/json/"+filename) as data_file:    
        for line in data_file.readlines():
            message_json = json.loads(line)
            try:
                message_json['media']
            except KeyError:
                try:
                    # is not a media
                    if 'http' in message_json['text']: continue # catch extra links
                    if message_json['from']['username'] == "ianan":
                        outfile.writelines( message_json['text'] + '\n')
                    continue
                except:
                    continue

