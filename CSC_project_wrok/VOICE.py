try:
    from googletrans import Translator
    from gtts import gTTS
    import tempfile
    import os
    import speech_recognition as sr

    language_mapping = {
        "english": "en",
        "spanish": "es",
        "french": "fr",
        "german": "de",
        "italian": "it",
        "portuguese": "pt",
        "russian": "ru",
        "chinese": "zh-CN",
        "japanese": "ja",
        "korean": "ko",
        "arabic": "ar",
        "hindi": "hi",
        "dutch": "nl",
        # Add more language mappings as needed
    }

    def recognize_speech():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak something...")
            audio = recognizer.listen(source)

        try:
            recognized_text = recognizer.recognize_google(audio)
            print("Recognized text:", recognized_text)
            return recognized_text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return None

    def get_target_language():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("In which language would you like to translate? Say the language name (e.g., 'French').")
            audio = recognizer.listen(source)

        try:
            target_language_name = recognizer.recognize_google(audio)
            return target_language_name
        except sr.UnknownValueError:
            print("Sorry, could not understand the target language.")
            return None

    def translate_text(text, target_language):
        translator = Translator()

        target_language_code = language_mapping.get(target_language.lower(), target_language)

        translated = translator.translate(text, dest=target_language_code)
        return translated.text

    def text_to_speech(text, lang):
        tts = gTTS(text=text, lang=lang)

        temp_audio_path = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3").name
        tts.save(temp_audio_path)

        os.system(f"start {temp_audio_path}")

    if __name__ == '__main__':
        input_text = recognize_speech()

        if input_text:
            target_language = get_target_language()

            if target_language:
                if target_language.lower() in language_mapping:
                    target_language_code = language_mapping[target_language.lower()]
                    translated_text = translate_text(input_text, target_language_code)
                    print("Translated text:", translated_text)

                    text_to_speech(translated_text, target_language_code)
                else:
                    print("Language not found in the mapping.")
except:
    print("Program has ended unexpectedly")
finally:
    print("Program has ended")