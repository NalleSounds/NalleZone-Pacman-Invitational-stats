# idea is to make GUI to prompt data from file, so far it's just messing around

import json

with open('matches.json') as matches_file:
    file_contents = matches_file.read()

print(file_contents)

parsed_file = json.loads(file_contents)
