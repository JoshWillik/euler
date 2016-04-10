import json

with open('challenges.json', 'r') as f:
    challenges = json.load(f)

with open('solutions.json', 'r') as f:
    solutions = json.load(f)

with open('README.md', 'w') as f:
    print('# Josh Does Project Euler\n', file=f)
    for i, challenge in enumerate(challenges):
        i += 1
        print('## ✘ {id}: {title}\n'.format(**challenge), file=f)
        print('{description}\n'.format(**challenge), file=f)

        try:
            solved_with = solutions[str(i)]['solutions']
            if len(solved_with):
                print('### Solutions\n', file=f)
                for solution in solved_with:
                    print('- [{language}](challenges/{index}/{language})\n'.format(language=solution, index=i), file=f)
        except Exception as e: pass
