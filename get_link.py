import json
import requests

API_KEY = "40d1649f-0493-4b70-98ba-98533de7710b"


def get_link(filePath):
    try:
        searchUrl = 'https://yandex.ru/images/search'
        files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
        params = {'rpt': 'imageview', 'format': 'json',
                  'request': '{"blocks": [{"block": "b-page_type_search-by-image__link"}]}',
                  'apikey': API_KEY}
        response = requests.post(searchUrl, params=params, files=files)
        query_string = json.loads(response.content)['blocks'][0]['params']['url']
        img_search_url = searchUrl + '?' + query_string
        return img_search_url
    except Exception as e:
        return e
