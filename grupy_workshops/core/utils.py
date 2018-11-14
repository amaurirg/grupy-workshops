import json
from requests import post
from grupy_workshops.settings import TOKEN


lista = ["Python Básico", "HTML", "Django", "Docker"]


def message1(chat_id):
    send_message("Lista de possíveis futuros workshops do Grupy-SP:\n\n" +
                 "\n".join(nome for nome in lista), chat_id)


def options_keyboard():
    reply_markup = {"inline_keyboard":
                        [
                            [{"text": "Ver lista de workshops", "callback_data": "1"}],
                            [{"text": "Votar em um workshop", "callback_data": "2"}],
                            [{"text": "Adicionar um workshop", "callback_data": "3"}]
                        ]
    }
    return json.dumps(reply_markup)


def send_message(text, chat_id, reply_markup=options_keyboard()):
    data = {'chat_id': chat_id, 'text': text, 'reply_markup': reply_markup}
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    post(url, data=data)


def voting_list(chat_id):
    reply_markup = {"inline_keyboard": [[{"text": i, "callback_data": f"script {i}"}] for i in lista]}
    send_message("Escolha um workshop que você gostaria que o Grupy-SP fizesse:",
                 chat_id, json.dumps(reply_markup))


def add_workshop(chat_id, workshop):
    send_message("Tem certeza que deseja adicionar essa sugestão de workshop?", chat_id)


def chosen_options(chat_id, chosen_data,  workshop=None):
    if chosen_data == '1':
        message1(chat_id)
    elif chosen_data == '2':
        voting_list(chat_id)
    elif chosen_data == '3':
        add_workshop(chat_id, workshop)
    # elif chosen_date in lista:
    #     lista.append(chosen_date)
    else:
        send_message(f"Você votou em {chosen_data}", chat_id)
        # message1(chat_id)