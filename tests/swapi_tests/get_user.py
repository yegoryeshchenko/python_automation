# import requests
#
# import json
#
# response = requests.get(url='https://swapi.dev/api/people/1/')
#
# status_code = response.status_code
# text = response.text
# headers = dict(response.headers)
#
# response_json = response.json()  #   == json.loads(response.text)
#
#
# print('status_code', status_code)
# print('headers', headers)
# print('-'*80)
# print('text', text)
# print('-'*80)
# print('response_json', response_json)