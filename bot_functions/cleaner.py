def config_clean(config: dict):
    """
    Cleans config from extra intents, examples or respnses\n
    :param config: config of data
    :return: clean config of data
    """
    false_template = []
    for intent, value in config['intents'].items():
        if 'responses' in value and 'examples' in value:
            value['responses'] = list_cleaner(value['responses'])
            value['examples'] = list_cleaner(value['examples'])
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


def clean(text: str):
    """
    Changing your text, removes extra symbols\n
    :param text: string of text for cleaning
    :return: clean text, whore symbols are in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    """
    return ''.join([symbol for symbol in text.lower() if symbol in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '])


def list_cleaner(data: list):
    """
    Changing your list of strings, removes extra symbols from it\n
    :param data: list of strings
    :return: list of strings, cleaned from extra symbols
    """
    for_delete = []
    for id in range(len(data)):
        data[id] = clean(data[id])
        if data[id] == '':
            for_delete.append(id)
    for_delete.reverse()
    for id in for_delete:
        data.pop(id)
    return list(set(data))
