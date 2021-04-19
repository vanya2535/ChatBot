import random
import json
import nltk
from bot_functions.cleaner import config_clean, clean
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier


def CV(config: dict):
    classifier = RandomForestClassifier()
    vectorizer = CountVectorizer()
    x = []
    y = []



def get_config(path: str):
    """
    Gets config from .json file\n
    :param path: path to .json file
    :return: clean config of bot
    """
    with open(path, 'r') as config_file:
        config = json.load(config_file)
    config = config_clean(config)
    return config


def typo_check(text: str, example: str):
    """
    Checks text for typos and matches against the example
    :param text: text for checking
    :param example: example to matching against the text
    :return: True or False, match or didn`t match
    """
    return nltk.edit_distance(text, example) / len(example) < 0.35


def get_response(question: str, config: dict):
    """
    Checks intents in config for examples, that match the question\n
    :param question: your question
    :param config: config of bot
    :return: response for question
    """
    question = clean(question)
    for intent, value in config['intents'].items():
        for example in value['examples']:
            if typo_check(question, example):
                return random.choice(value['responses']).capitalize()
    else:
        return 'Я тебя не понимаю'
