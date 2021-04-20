import nltk


def wrong_config_clean(config: dict):
    """
    Cleans config from extra intents, examples or respnses\n
    This function is actual for wrong_config.json\n
    :param config: config of data
    :return: clean config of data
    """
    false_template = []
    for intent, value in config['intents'].items():
        if 'responses' in value and 'examples' in value:
            value['responses'] = list_clean(value['responses'])
            value['examples'] = list_clean(value['examples'])
            if len(list(value.keys())) > 2:
                for sample in list(value.keys()):
                    if sample != 'responses' and sample != 'examples':
                        value.pop(sample)
            if len(value['responses']) == 0 or len(value['examples']) == 0:
                false_template.append(intent)
        else:
            false_template.append(intent)
    for falseIntent in false_template:
        config['intents'].pop(falseIntent)
    return config


def config_clean(config: dict):
    """
    Cleans config from extra intents, examples or respnses\n
    This function is actual for wrong_config.json\n
    :param config: config of data
    :return: clean config of data
    """
    for value in config['intents'].values():
        value['responses'] = nltk_list_clean(value['responses'])
        value['examples'] = nltk_list_clean(value['examples'])
    return config


def text_clean(text: str):
    """
    Changing your text, removes extra symbols\n
    :param text: string of text for cleaning
    :return: clean text, whore symbols are in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    """
    return ''.join([symbol for symbol in text.lower() if symbol in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-, '])


def list_clean(data: list):
    """
    Changing your list of strings, removes extra symbols from it\n
    :param data: list of strings
    :return: list of strings, cleaned from extra symbols
    """
    for_delete = []
    for id in range(len(data)):
        data[id] = text_clean(data[id])
        if data[id] == '':
            for_delete.append(id)
    for_delete.reverse()
    for id in for_delete:
        data.pop(id)
    return list(set(data))


def typo_check(text: str, example: str):
    """
    Checks text for typos and matches against the example
    :param text: text for checking
    :param example: example to matching against the text
    :return: True or False, match or didn`t match
    """
    return nltk.edit_distance(text, example) / len(example) < 0.2


def nltk_list_clean(data: list):
    """
    Changing your list of strings, removes extra words
    :param data: list of strings
    :return: list of strings, cleaned from extra words
    """
    data = list_clean(data)
    for_delete = set()
    for elem_id in range(len(data)):
        for id in range(elem_id + 1, len(data)):
            if typo_check(data[elem_id], data[id]):
                for_delete.add(id)
    for_delete = list(for_delete)
    for_delete.sort()
    for_delete.reverse()
    for id in for_delete:
        data.pop(id)
    return data


def str_list(string: str):
    """
    Transform string of words to list of words\n
    :param string: string of words
    :return: list of words
    """
    st_list = string.split(', ')
    return st_list
