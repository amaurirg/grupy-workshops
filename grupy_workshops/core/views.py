import json
import grupy_workshops.core.utils as utils
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from grupy_workshops.core.models import Interactions


def home(request):
    return render(request, "index.html")


@csrf_exempt
def event(requests):
    json_list = json.loads(requests.body)
    print(json_list)

    a, b = json_list
    results = json_list[b]['from']
    first_name = results['first_name']
    larst_name = results['last_name']
    username = results['username']
    chat_id = results['id']

    if not b == 'callback_query':
        text_message = json_list['message']['text']
        utils.send_message("Escolha uma opção para futuros workshops do Grupy-SP", chat_id)
    else:
        chosen_data = json_list['callback_query']['data']
        # resp = Interactions.objects.get(command=f"script {chosen_data}")
        # utils.send_message(f"{resp.output} {chosen_data}", chat_id)
        utils.chosen_options(chat_id, chosen_data)

    # print(chat_id)
    # utils.send_message('{}, sua mensagem ao contrário é\n{}'.format(first_name, text_message[::-1]), chat_id)
    # teclado = utils.build_keyboard()
    # chat_id = '200598266'
    # utils.send_message("Teclado", chat_id)
    # if text_message == "Texto1":
    #     utils.send_message("O botão texto 1 foi pressionado", chat_id)
    # print(first_name)
    return HttpResponse()
