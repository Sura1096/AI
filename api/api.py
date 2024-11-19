import requests
import json

from config.config import api_settings


def get_api_token() -> str:
    """
    Возвращает Access token.

    :return: Access token.
    """
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    payload = {
        'scope': 'GIGACHAT_API_PERS'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': 'a86e29ca-921b-4a00-859a-2c13db984b8b',
        'Authorization': f'Basic {api_settings.AUTH_KEY}'
    }

    response = requests.post(url, headers=headers, data=payload, verify=False)
    return response.json()['access_token']


def get_chat_completion(token: str, user_message: str) -> str:
    """
    Возвращает ответ на запрос.

    :param token: Access token.
    :param user_message: Запрос от пользователя.
    :return: Ответ на запрос от GigaChat.
    """
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    payload = json.dumps({
        "model": "GigaChat",
        "messages": [
            {
                "role": "user",
                "content": user_message
            }
        ],
        "n": 1,
        "stream": False,
        "max_tokens": 512,
        "repetition_penalty": 1,
        "update_interval": 0
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    response = requests.post(url, headers=headers, data=payload, verify=False)
    return response.json()['choices'][0]['message']['content']
