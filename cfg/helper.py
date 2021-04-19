import json


def str_transform(string: str):
    st_list = string.split(', ')
    return st_list


def get_examples(config_path: str, intent: str, eor: str):
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    if intent in config['intents']:
        return config['intents'][intent][eor]
    else:
        return 'Sorry'


print(list(set(word.lower() for word in get_examples('wrong_config.json', 'bye', 'examples'))))
