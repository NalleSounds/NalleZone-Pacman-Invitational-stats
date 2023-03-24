# GUI to prompt data from file

import json

with open('matches.json') as matches_file:
    file_contents = matches_file.read()

print(file_contents)

parsed_file = json.loads(file_contents)
