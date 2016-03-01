import os
import json
from collections import OrderedDict

file_list = [int(name) for name in os.listdir('challenges')]
file_list.sort()

challenges = []
for id in file_list:
    with open('challenges/' + str(id), 'r') as f:
        lines = f.readlines()
        challenges.append(OrderedDict({
            'id': id,
            'url': 'https://projecteuler.net/problem={}'.format(id),
            'title': lines[0].strip(),
            'description': '\n'.join([line for line in lines[1:] if line.strip()]).strip()
        }))

with open('challenges.json', 'w') as f:
    json.dump(challenges, f, indent=4)
