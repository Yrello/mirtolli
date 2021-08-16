# -*- coding: utf-8 -*-
import requests
from flask import Flask, request
import logging
import json

app = Flask(__name__)



#token = 'Yto6i3oaZeJlpklLiUhzgpG8s0RMLyBxLoYJ3Car6QQ'
token = ''
response = requests.get('https://api.salesap.ru/api/v1/'+token+'/')
response.encoding = 'utf-8'
#print(response.content.decode('utf8'))
print(response.headers,'\n\n\n')

response = requests.get('https://app.salesap.ru/api/v1/'+token+'/contacts/1')
#print(response.content.decode('utf8'))
print(response)

@app.route('/install_webhook',methods=['GET'])
def get_token2():
    global token
    t = request.args['token']
    print(t)
    token = t
    return 200



@app.route('/',methods=['GET'])
def get_token():
    t = request.args['token']
    print(t)
    return ''

@app.route('/post', methods=['POST'])
# Функция получает тело запроса и возвращает ответ.
# Внутри функции доступен request.json - это JSON,
# который отправила нам Алиса в запросе POST
def main():
    logging.info(f'Request: {request.json!r}')
    # Начинаем формировать ответ, согласно документации
    # мы собираем словарь, который потом при помощи
    # библиотеки json преобразуем в JSON и отдадим Алисе
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }

    # Отправляем request.json и response в функцию handle_dialog.
    # Она сформирует оставшиеся поля JSON, которые отвечают
    # непосредственно за ведение диалога
    # handle_dialog(request.json, response)
    logging.info(f'Response:  {response!r}')
    # Преобразовываем в JSON и возвращаем
    return json.dumps(response)

if __name__ == '__main__':
    app.run(port=359)
