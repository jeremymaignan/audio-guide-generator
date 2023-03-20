import pyttsx3

class Audio:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')

        # Set EN_uk voice
        self.engine.setProperty('voice', voices[7].id)

        # Set speed
        rate = self.engine.getProperty('rate')
        self.engine.setProperty(rate, 150)

    def save_audio_file(self, text, filename):
        self.engine.save_to_file(text, '{}'.format(filename))
        self.engine.runAndWait()

