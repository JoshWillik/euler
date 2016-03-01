import json

with open('challenges.json', 'r') as f:
    challenges = json.load(f)

with open('README.md', 'w') as f:
    for challenge in challenges:
        print('✘ {id}: {title}'.format(**challenge), file=f)
        print('', file=f)
        print('{description}'.format(**challenge), file=f)
        print('', file=f)
