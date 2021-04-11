def config_clean(config: dict):
    false_template = []
    for intent, value in config['intents'].items():
        if 'responses' in value and 'examples' in value:
            value['responses'] = list(set(value['responses']))
            value['examples'] = list(set(value['examples']))
            if len(list(value.keys())) > 2:
                for sample in list(value.keys()):
                    if sample != 'responses' and sample != 'examples':
                        value.pop(sample)
        else:
            false_template.append(intent)
    for falseIntent in false_template:
        config['intents'].pop(falseIntent)
    return config
