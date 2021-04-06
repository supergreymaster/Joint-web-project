from requests import post
import json
import base64


def get_iam_token(iam_url, oauth_token):
    response = post(iam_url, json={"yandexPassportOauthToken": oauth_token})
    json_data = json.loads(response.text)
    if json_data is not None and 'iamToken' in json_data:
        return json_data['iamToken']
    return None


def request_analyze(vision_url, iam_token, folder_id, image_data):
    response = post(vision_url, headers={'Authorization': 'Bearer ' + iam_token}, json={
        'folderId': folder_id,
        'analyzeSpecs': [
            {
                'content': image_data,
                'features': [
                    {
                        'type': 'TEXT_DETECTION',
                        'textDetectionConfig': {'languageCodes': ['en', 'ru']}
                    }
                ],
            }
        ]})
    return response.text


def get_text(image_path):  # вызывать ее, в аргументы путь в формате строки. Например 'test.png'
    folder_id = 'b1gda6o00s0iueac3b1c'
    oauth_token = 'AQAAAAAVdxsdAATuwSCvXz4_A0kLkDik2MpRZ1I'
    image_path = image_path

    iam_url = 'https://iam.api.cloud.yandex.net/iam/v1/tokens'
    vision_url = 'https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze'

    iam_token = get_iam_token(iam_url, oauth_token)
    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')
    response_text = request_analyze(vision_url, iam_token, folder_id, image_data)
    result = json.loads(response_text)
    ready_text = ''
    for first_result in result:
        for second_result in result[first_result]:
            for third_result in second_result:
                for fourth_result in second_result[third_result]:
                    for fifth_result in fourth_result:
                        for seventh_result in fourth_result[fifth_result]:
                            for eighth_result in fourth_result[fifth_result][seventh_result]:
                                for ninth in eighth_result:
                                    for tenth in eighth_result[ninth]:
                                        if isinstance(tenth, dict):
                                            for eleventh in tenth:
                                                if isinstance(tenth[eleventh], list):
                                                    for twelfth in tenth[eleventh]:
                                                        for thirteenth in twelfth['words']:
                                                            ready_text = ready_text + thirteenth['text'] + ' '
                                                        ready_text += '\n'
    ready_text = ready_text[:len(ready_text) - 2]
    return ready_text
