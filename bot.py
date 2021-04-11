from func import get_response, get_config

bot_config = get_config('bot_config.json')
question = input()
while question != 'выход':
    print(get_response(question, bot_config))
    question = input()
