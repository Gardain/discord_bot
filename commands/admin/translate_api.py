import requests


def translate_api(lang_pair, text):
    url = "https://api.mymemory.translated.net/get"
    querystring = {"langpair": lang_pair, "q": text}
    response = requests.request("GET", url, params=querystring).json()
    return response["responseData"]["translatedText"].capitalize()
