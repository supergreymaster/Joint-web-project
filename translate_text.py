import requests
import ast
from get_text import get_iam_token
from detect_language import detect_language

folderId = 'b1gda6o00s0iueac3b1c'
iam_url = 'https://iam.api.cloud.yandex.net/iam/v1/tokens'
oauth_token = 'AQAAAAAVdxsdAATuwSCvXz4_A0kLkDik2MpRZ1I'

'''На вход функции дается текст'''
'''Функция переведет на противоположный язык'''
'''На данный момент - это русский и английский'''
'''Добавить другие языки не проблема, но разберемся с этим позже'''


def translate_text(text):
    sourceLang = detect_language(text)
    targetLang = 'ru' if sourceLang == 'en' else 'en'
    iam_token = get_iam_token(iam_url, oauth_token)
    v_url = 'https://translate.api.cloud.yandex.net/translate/v2/translate'
    res = requests.post(v_url, headers={'Authorization': 'Bearer ' + iam_token}, json={
        "sourceLanguageCode": sourceLang,
        "targetLanguageCode": targetLang,
        "texts": [
            text
        ],
        "folderId": folderId
    })
    return ast.literal_eval(res.text)['translations'][0]['text']
