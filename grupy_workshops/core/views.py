import json
import grupy_workshops.core.utils as utils
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "index.html")


@csrf_exempt
def event(requests):
    json_list = json.loads(requests.body)
    print(json_list)
    # print(json_list.get('callback_query'))
    # first_name = json_list.get('first_name')
    # first_name = json_list['message']['chat']['first_name']

    if not json_list.get('callback_query'):
        chat_id = json_list['message']['chat']['id']
        text_message = json_list['message']['text']
        utils.send_message("Nenhum botão foi pressionado", chat_id)
    else:
        chat_id = json_list['callback_query']['message']['chat']['id']
        data = json_list['callback_query']['data']
        utils.send_message(f"O botão texto {data} foi pressionado", chat_id)

    # print(chat_id)
    # utils.send_message('{}, sua mensagem ao contrário é\n{}'.format(first_name, text_message[::-1]), chat_id)
    # teclado = utils.build_keyboard()
    # chat_id = '200598266'
    utils.send_message("Teclado", chat_id)
    # if text_message == "Texto1":
    #     utils.send_message("O botão texto 1 foi pressionado", chat_id)
    # print(first_name)
    return HttpResponse()
