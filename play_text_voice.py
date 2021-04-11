import pyttsx3


def play_text(rate, volume=1):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    with open('voice_text.mp3', 'r', encoding='cp1252') as voice_text:
        data = voice_text.read()
        engine.say(data, sync=True)
        engine.runAndWait()


play_text(150, 1)
