import json

config = {
    'intents': {
        'hello': {
            'examples': ['Привет', 'Здравствуй', 'Здравствуйте', 'Здарова', 'Приветик', 'Хай', 'добрый день',
                         'всем привет', 'приветствую вас', 'здорова', 'интересное кино', 'здравствуйте всем',
                         'мое почтение', 'здравия желаю', 'рад видеть', 'приветствую', 'салам', 'хой', 'здравствуйте',
                         'добрый день', 'здравствуй', 'приветик', 'хай', 'ку', 'шелом', 'физкульт-привет', 'хаюшки',
                         'саламчик', 'бонжур', 'здарова', 'хола', 'здравия желаю', 'прив', 'дорого утра', 'привед',
                         'салам!', 'здарова!', 'салют', 'хола', 'шолом', 'моё почтение', 'йо', 'алоха', 'здравствуй!',
                         'здрасти', 'приветики', 'шалом', 'ку', 'хелло', 'мое почтение', 'здарова', 'привет',
                         'бонжур', 'хаюшки', 'здравствуйте', 'ёу', 'рад встрече', 'ку!', 'доброе утро!', 'утречко!',
                         'дарова', 'салам алейкум!', 'салам', 'здравствуй', 'доброго вечера', 'хеллоу', 'здрасте',
                         'давно не виделись', 'привет!', 'конничива', 'салютик', 'хэллоу', 'добрый вечер',
                         'дратути', 'приветик', 'здравия желаю!', 'хэй', 'доров', 'доброго времени суток!',
                         'добрый день!', 'здраствуйте', 'хай!', 'даров', 'хэлло', 'йоу', 'доброго дня, дружище',
                         'здравствуйте!', 'привет-медвед', 'хай', 'приветики пистолетики', 'день добрый',
                         'приветствую', 'вечер добрый', 'позвольте поприветствовать вас', 'здрасьте',
                         'халоу', 'дароу', 'пламенный привет', 'физкульт-привет', 'хэлоу', 'приветствую вас!',
                         'доброе утро', 'приветствую вас', 'добрый день', 'хелоу', 'хаюхай', 'приветушки',
                         'приветули', 'здоровенько', 'здарова', 'доброго времечка', 'салют!', 'хеллоу!',
                         'доброго утра', 'доброго дня', 'приветствую!'],
            'responses': ['Привет', 'Здравствуй', 'Здравствуйте', 'Здарова', 'Приветик', 'Хай', 'добрый день',
                          'всем привет', 'приветствую вас', 'здорова', 'интересное кино', 'здравствуйте всем',
                          'мое почтение', 'здравия желаю', 'рад видеть', 'приветствую', 'салам', 'хой', 'здравствуйте',
                          'добрый день', 'здравствуй', 'приветик', 'хай', 'ку', 'шелом', 'физкульт-привет', 'хаюшки',
                          'саламчик', 'бонжур', 'здарова', 'хола', 'здравия желаю', 'прив', 'дорого утра', 'привед',
                          'салам!', 'здарова!', 'салют', 'хола', 'шолом', 'моё почтение', 'йо', 'алоха', 'здравствуй!',
                          'здрасти', 'приветики', 'шалом', 'ку', 'хелло', 'мое почтение', 'здарова', 'привет',
                          'бонжур', 'хаюшки', 'здравствуйте', 'ёу', 'рад встрече', 'ку!', 'доброе утро!', 'утречко!',
                          'дарова', 'салам алейкум!', 'салам', 'здравствуй', 'доброго вечера', 'хеллоу', 'здрасте',
                          'давно не виделись', 'привет!', 'конничива', 'салютик', 'хэллоу', 'добрый вечер',
                          'дратути', 'приветик', 'здравия желаю!', 'хэй', 'доров', 'доброго времени суток!',
                          'добрый день!', 'здраствуйте', 'хай!', 'даров', 'хэлло', 'йоу', 'доброго дня, дружище',
                          'здравствуйте!', 'привет-медвед', 'хай', 'приветики пистолетики', 'день добрый',
                          'приветствую', 'вечер добрый', 'позвольте поприветствовать вас', 'здрасьте',
                          'халоу', 'дароу', 'пламенный привет', 'физкульт-привет', 'хэлоу', 'приветствую вас!',
                          'доброе утро', 'приветствую вас', 'добрый день', 'хелоу', 'хаюхай', 'приветушки',
                          'приветули', 'здоровенько', 'здарова', 'доброго времечка', 'салют!', 'хеллоу!',
                          'доброго утра', 'доброго дня', 'приветствую!']
        },
        'bye': {
            'examples': ['Пока', 'До свидания', 'До встречи', 'Увидимся', 'Покеда', 'Гуд бай', 'Досвидос',
                         'до встречи', 'пока', 'бывай', 'до вечера', 'всего хорошего', 'до завтра', 'всего доброго',
                         'до новых встреч', 'встретимся', 'до свиданья', 'удачи', 'прощевайте', 'всего наилучшего',
                         'до скорого', 'до скорой встречи', 'до связи', 'счастливо', 'увидимся', 'не поминайте лихом',
                         'разрешите откланяться', 'позвольте откланяться', 'счастливо оставаться',
                         'до скорого свидания', 'созвонимся', 'пересечемся', 'не поминай лихом', 'свидимся',
                         'маме привет', 'бай', 'целую ручки', 'спишемся', 'чао', 'честь имею кланяться', 'до созвона',
                         'позвольте попрощаться', 'разрешите попрощаться', 'всего лучшего', 'гуд-бай', 'ауфидерзейн',
                         'прощевай', 'гудбайте', 'словимся', 'ариведерче', 'сайонара', 'прости-прощай', 'адью',
                         'покедова', 'покеда', 'бай-бай', 'удачного дня', 'разрешите откланяться', 'пока-пока',
                         'до встречи', 'хорошего дня', 'доброй ночи', 'давай до свидания', 'до связи',
                         'счастливо тебе!', 'до свидание', 'бывай', 'давай', 'гуд бай', 'чао', 'прощевай', 'чао-какао',
                         'мне пора уходить', 'я еще вернусь', 'доброго вечера', 'пока', 'прощай', 'досвидос',
                         'на связи', 'всего хорошего!', 'бай-бай', 'бывай', 'бай', 'до скорого', 'аревуар',
                         'ауфидерзейн', 'всего наилучшего', 'досвидос!', 'счастливо оставаться', 'до скорого',
                         'поки', 'аривидерчи', 'гудбай', 'всего доброго', 'досвидули', 'до скорой встречи', 'пока',
                         'всего хорошего', 'пакеда', 'было приятно побеседовать', 'гуд-бай', 'до свидания',
                         'увидимся', 'до новых встреч', 'до скорой встречи', 'ариведерчи', 'покеда', 'до скорых встреч',
                         'не скучай'],
            'responses': ['Пока', 'До свидания', 'До встречи', 'Увидимся', 'Покеда', 'Гуд бай', 'Досвидос',
                          'до встречи', 'пока', 'бывай', 'до вечера', 'всего хорошего', 'до завтра', 'всего доброго',
                          'до новых встреч', 'встретимся', 'до свиданья', 'удачи', 'прощевайте', 'всего наилучшего',
                          'до скорого', 'до скорой встречи', 'до связи', 'счастливо', 'увидимся', 'не поминайте лихом',
                          'разрешите откланяться', 'позвольте откланяться', 'счастливо оставаться',
                          'до скорого свидания', 'созвонимся', 'пересечемся', 'не поминай лихом', 'свидимся',
                          'маме привет', 'бай', 'целую ручки', 'спишемся', 'чао', 'честь имею кланяться', 'до созвона',
                          'позвольте попрощаться', 'разрешите попрощаться', 'всего лучшего', 'гуд-бай', 'ауфидерзейн',
                          'прощевай', 'гудбайте', 'словимся', 'ариведерче', 'сайонара', 'прости-прощай', 'адью',
                          'покедова', 'покеда', 'бай-бай', 'удачного дня', 'разрешите откланяться', 'пока-пока',
                          'до встречи', 'хорошего дня', 'доброй ночи', 'давай до свидания', 'до связи',
                          'счастливо тебе!', 'до свидание', 'бывай', 'давай', 'гуд бай', 'чао', 'прощевай', 'чао-какао',
                          'мне пора уходить', 'я еще вернусь', 'доброго вечера', 'пока', 'прощай', 'досвидос',
                          'на связи', 'всего хорошего!', 'бай-бай', 'бывай', 'бай', 'до скорого', 'аревуар',
                          'ауфидерзейн', 'всего наилучшего', 'досвидос!', 'счастливо оставаться', 'до скорого',
                          'поки', 'аривидерчи', 'гудбай', 'всего доброго', 'досвидули', 'до скорой встречи', 'пока',
                          'всего хорошего', 'пакеда', 'было приятно побеседовать', 'гуд-бай', 'до свидания',
                          'увидимся', 'до новых встреч', 'до скорой встречи', 'ариведерчи', 'покеда',
                          'до скорых встреч',
                          'не скучай']
        },
        'how are you': {
            'examples': ['Как дела?', 'Как твои дела?', 'Как сам?', 'Как ты себя чувствуешь?', 'Как у тебя дела?',
                         'Как прошел день?', 'Как настроение?', 'как поживаешь', 'Как оно?', 'Чё кого',
                         'как жизнь', 'Как вы?', 'как сам', 'как себя чувствуешь', 'как настроение',
                         'что нового', 'как прошёл день', 'ты как', 'как жизнь', 'как жизнь молодая', 'как делишки'],
            'responses': ['Нормально', 'Бывало и лучше', 'Не очень', 'Ничего особого', 'Все круто',
                          'У меня все хорошо', 'Все замечательно', 'Нормально.', 'Неплохо', 'Хорошо',
                          'Все идет неплохо. Пытаюсь научиться разговаривать с людьми.', 'Без вас скучно.',
                          'Великолепно', 'Не жалуюсь', 'Могло бы быть и лучше', 'Порядок', 'Сойдет', 'как обычно',
                          'нормуль', 'все хорошо', 'да так', 'всё путём', 'по-тихоньку',
                          'работаю, что не может не радовать', 'хорошо', 'да нормально', 'да как-то никак',
                          'у меня все ок', 'сойдет', 'всё круто', 'супер', 'ой не спрашивай', 'супер-пупер',
                          'лучше не было', 'всё прекрасно', 'не жалуюсь', 'все ок', 'жизнь - боль', 'так себе',
                          'более-менее', 'великолепно', 'все отлично', 'нормально', 'потихоньку',
                          'дела у прокурора, а я бот', 'норм', 'могло бы быть и лучше',
                          'было плохо, пока со мной не заговорил добрый человек', 'замечательно', 'лучше всех']

        },
        'who are you': {
            'examples': ['Ты кто?', 'Кто ты?', 'Кто ты такой?', 'Что ты такое?', 'с кем я говорю', 'как твоё имя',
                         'как я могу к тебе обращаться', 'как тебя зовут', 'ты кто', 'твое имя', 'звать тебя как',
                         'как зовут', 'кем будешь', 'назови себя', 'представься', 'кто такой', 'у тебя есть имя'],
            'responses': ['Я - робот', 'Я - тупой искуственный интеллект', 'Я - бот', 'Я - машина', 'Я не знаю',
                          'я - простенький чат-бот', 'я ваш помощник', 'я - чат-бот', 'я - искусственный интелект',
                          'я тот, кого трудно найти, легко потерять и невозможно забыть', 'я - программа',
                          'я точно не человек', 'не скажу', 'пока не придумал', 'я - виртуальный ассистент',
                          'я - гуль', 'компьютерный мозг', 'я - бот', 'я - полезная штука', 'ваш чат бот',
                          'я тот, кто вам нужен', 'не тебе это спрашивать, безкодное создание',
                          'твой собеседник', 'бот, чат бот', 'точно не сири и не алиса', 'зови меня просто - хозяин',
                          'чат-бот', 'я - будущий черный властелин вселенной', 'я бот', 'ваш персональный помощник',
                          'я - чатбот', 'я - твой повелитель', 'тот, с кем вы не будете грустить']
        }
    }
}


with open('my_bot_config.json', 'w') as config_file:
    json.dump(config, config_file)
