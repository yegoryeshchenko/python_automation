import os
import json

from constants import BASE_PATH


results_folder_path = os.path.join(BASE_PATH, 'results')  # створить вірний шлях в поточній ОС

result_dictionary = {}

for path_, folders, files in os.walk(results_folder_path):

    for file_path in files:

        if not file_path.endswith('result.json'):
            continue

        with open(os.path.join(path_, file_path)) as f:
            file_content_json = json.load(f)

        epic = 'no_epic'
        feature = 'no_feature'
        story = 'no_story'

        status = file_content_json.get('status', 'no_status')

        for label in file_content_json.get('labels', []):

            if label.get('name') == 'epic':
                epic = label['value']

            if label.get('name') == 'feature':
                feature = label['value']

            if label.get('name') == 'story':
                story = label['value']


        # epic -> feature -> story
        if epic not in result_dictionary:
            result_dictionary[epic] = {}

        if feature not in result_dictionary[epic]:
            result_dictionary[epic][feature] = {}

        if story not in result_dictionary[epic][feature]:
            result_dictionary[epic][feature][story] = {}

        if status not in result_dictionary[epic][feature][story]:
            result_dictionary[epic][feature][story][status] = 0

        result_dictionary[epic][feature][story][status] += 1

print(json.dumps(result_dictionary, indent=4))


