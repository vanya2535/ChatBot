import random
import json
from cfg_clean import config_clean


def get_config(path: str):
    with open(path, 'r') as config_file:
        config = json.load(config_file)
    config = config_clean(config)
    return config


def get_response(question: str, config: dict):
    for intent, value in config['intents'].items():
        for example in value['examples']:
            if question == example:
                return random.choice(value['responses'])