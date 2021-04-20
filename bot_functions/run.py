import random
import json
from bot_functions.cleaner import wrong_config_clean, text_clean, typo_check, config_clean
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier


def get_config(path: str):
    """
    Gets config from .json file\n
    :param path: path to .json file
    :return: clean config of bot
    """
    with open(path, 'r') as config_file:
        config = json.load(config_file)
    if path.find('wrong') != -1:
        config = wrong_config_clean(config)
    else:
        config = config_clean(config)
    return config


def get_response(question: str, config: dict):
    """
    Checks intents in config for examples, that match the question\n
    :param question: your question
    :param config: config of bot
    :return: response for question
    """
    question = text_clean(question)
    for intent, value in config['intents'].items():
        for example in value['examples']:
            if typo_check(question, example):
                return random.choice(value['responses']).capitalize()
    else:
        return 'Я тебя не понимаю'
