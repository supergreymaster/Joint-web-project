import requests
import ast
from get_text import get_iam_token

folderId = 'b1gda6o00s0iueac3b1c'
iam_url = 'https://iam.api.cloud.yandex.net/iam/v1/tokens'
oauth_token = 'AQAAAAAVdxsdAATuwSCvXz4_A0kLkDik2MpRZ1I'

'''Это вспомогательная функция, она вызывается из translate_text автоматически'''


def detect_language(string):  # функция определяет язык текста
    iam_token = get_iam_token(iam_url, oauth_token)
    v_url = 'https://translate.api.cloud.yandex.net/translate/v2/detect'
    res = requests.post(v_url, headers={'Authorization': 'Bearer ' + iam_token}, json={
        "text": string,
        "languageCodeHints": [
            "ru",
            "en"
        ],
        "folderId": folderId
    })
    return ast.literal_eval(res.text)['languageCode']
