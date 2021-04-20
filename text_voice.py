from gtts import gTTS
import pyttsx3
from errors_module_for_text_voice import *


def save_text_as_mp3(text, file_name, lang):
    if text:
        voice = gTTS(text, lang=lang)
        voice.save(file_name)
    else:
        raise TextInvalidValue


def play_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.say(text)
    engine.runAndWait()


# save_text_as_mp3('Советский союз нерушимых республик!', 'test_voice_1.mp3', 'ru')
# play_text('Карл у Клары украл кораллы, Клара у Карла украла кларнет.')