import requests


def translate_file(file_name, lang_for_translate, lang_result):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
     
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20181204T063748Z.e91a70705695696d.b39566d90088909ff6e32030d64e63d7863b7381'

    try:
        with open(file_name, encoding='utf-8') as f:
            text_file = f.read()
    except FileNotFoundError as e:
        return print('Файл не был найден!', e)

    languages = lang_for_translate + '-' + lang_result

    params = {
        'key': key,
        'lang': languages,
        'text': text_file,
    }

    response = requests.post(url, data=params, timeout=30)
    assert response.status_code == 200, 'Введите язык в нужном формате языка. Например Русский = ru'
    body = response.json()
    translated_text = ' '.join(body.get('text', []))
    print(translated_text)
    with open(translated_file_name, 'w', encoding='utf-8') as tf:
        tf.write(translated_text)


if __name__ == '__main__':
    file_name = input('Введите имя файла: ')
    lang_for_translate = input('Введите язык документа: ').lower()
    lang_result = input('Введите на какой язык нужно перевести документ: ').lower()
    translated_file_name = 'translated_in_' + lang_result + '_from_' + file_name
    translate_file(file_name, lang_for_translate, lang_result)
