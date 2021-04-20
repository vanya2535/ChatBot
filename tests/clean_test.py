from timeit import timeit

nltk_list_cleaner = '''
from bot_functions.cleaner import nltk_list_cleaner
import json
with open('test_config.json', 'r') as config_file:
    config = json.load(config_file)
for value in config['intents'].values():
    value['responses'] = nltk_list_cleaner(value['responses'])
    value['examples'] = nltk_list_cleaner(value['responses'])
'''
