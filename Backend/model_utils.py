from deep_translator import GoogleTranslator

class Translator:
    def __init__(self):
        self.translator = GoogleTranslator(source="en", target="ta")

    def translate(self, text):
        return self.translator.translate(text)
