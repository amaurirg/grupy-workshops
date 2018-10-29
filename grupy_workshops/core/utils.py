import json
from requests import get, post
from decouple import config


TOKEN = config('TOKEN')


def send_message(text, chat_id, reply_markup=None):
    data = {'chat_id': chat_id, 'text': text, 'reply_markup': build_keyboard()}
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN)
    # if reply_markup:
    #     url = "{}&reply_markup={}".format(url, reply_markup)
    post(url, data = data)


def build_keyboard():
    # items = ['Lista', 'Votos']
    # keyboard = [[item] for item in items]
    # reply_markup = [{"keyboard": keyboard, "one_time_keyboard": True}
    reply_markup = {"inline_keyboard":
                        [
                            [{"text": "Texto 1", "callback_data": "1"}],
                            [{"text": "Texto 2", "callback_data": "2"}],
                            [{"text": "Texto 3", "callback_data": "3"},
                            {"text": "Texto 4", "callback_data": "4"}]
                        ]
    }
    return json.dumps(reply_markup)