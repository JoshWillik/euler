import json

with open('challenges.json', 'r') as f:
    challenges = json.load(f)

with open('solutions.json', 'r') as f:
    solutions = json.load(f)

with open('README.md', 'w') as f:
    print('# Josh Does Project Euler\n', file=f)
    for i, challenge in enumerate(challenges):
        print('## ✘ {id}: {title}\n'.format(**challenge), file=f)
        print('{description}\n'.format(**challenge), file=f)

        try:
            solved_with = solutions[str(i + 1)]['solutions']
            if len(solved_with):
                print('### Solutions', file=f)
                for solution in solved_with:
                    print('- {}'.format(solution), file=f)
        except Exception as e: pass
