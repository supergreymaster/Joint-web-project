from gtts import gTTS
import pyttsx3
from errors_module_for_text_voice import *


def save_text_as_mp3(text, file_name, lang):
    if text:
        voice = gTTS(text, lang=lang)
        voice.save(file_name)
    else:
        raise InvalidValue('text_error')


def play_text(text, lang):
    try:
        languages_id = {'ru': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0',
                        'en': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'}
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1)
        engine.setProperty('voice', languages_id[lang])
        engine.say(text)
        engine.runAndWait()
    except KeyError:
        raise InvalidValue('language_error', lang)
