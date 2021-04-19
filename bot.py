from bot_functions.run import get_response, get_config


def bot(config_path: str):
    bot_config = get_config(config_path)
    question = input()
    while question != 'выход':
        print(get_response(question, bot_config))
        question = input()


bot('cfg/my_bot_config.json')
