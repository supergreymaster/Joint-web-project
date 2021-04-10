from gtts import gTTS
from errors_module_for_text_voice import *


def voice_text(text, lang):
    if text:
        voice = gTTS(text, lang=lang)
        voice.save('voice_text.mp3')
        """Пока я писал этот код, я ориентировался на то, что файлов с озвучкой текста всегда будет один.
            Если это не так, и подразумевается, что таких файлов будет много, то я попробую что-то сделать с
            проблемой названия файла."""
    else:
        raise TextInvalidValue


voice_text('', 'asdads')