import json
from bot_functions.cleaner import nltk_list_clean


def get_examples(config_path: str, intent: str, eor: str):
    """
    Gives 'examples' or 'responses' from chosen intent in config\n
    :param config_path: path to config
    :param intent: what intent we looking for
    :param eor: 'examples' or 'responses'
    :return: config['intents'][intent][eor] - list of intent elements
    """
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    if intent in config['intents']:
        return config['intents'][intent][eor]
    else:
        return 'Sorry'


def get_intents(config_path: str):
    """
    Show intent`s variety from config\n
    :param config_path: path to config
    """
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    for intent in config['intents'].keys():
        print(intent)


def search(config_path: str, search_words: list):
    """
    Searching your words in config\n
    :param config_path: path to config
    :param search_words: list of words
    :return: list of intents, consists of your words
    """
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    match = set()
    for intent, value in config['intents'].items():
        for word in search_words:
            if 'responses' in value and 'examples' in value:
                if word in value['responses'] or word in value['examples']:
                    match.add(intent)
    return list(match)


def get_data(config_path: str, search_list: list):
    """
    Give you lists of 'examples' and 'responses' of intents in search_list from config\n
    :param config_path: path to config
    :param search_list: list of intents to search
    :return: dictionary of 'examples' and list of 'responses'
    """
    examples_result = []
    responses_result = []
    for intent in search_list:
        examples_result += get_examples(config_path, intent, 'examples')
        responses_result += get_examples(config_path, intent, 'responses')
    examples_result = nltk_list_clean(examples_result)
    responses_result = nltk_list_clean(responses_result)
    intent = {
        'examples': examples_result,
        'responses': responses_result
    }
    return intent


def delete(config_path: str, intents: list):
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    for intent in intents:
        config['intents'].pop(intent)
    with open(config_path, 'w') as config_file:
        json.dump(config, config_file)
    return 'Удалено ' + str(len(intents)) + ' элементов'
