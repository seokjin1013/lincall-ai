import speech_recognition as sr

class STT:
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300

    def __new__(cls, path):
        korean_audio = sr.AudioFile(path)

        with korean_audio as source:
            data = cls.recognizer.record(source)

        return cls.recognizer.recognize_google(audio_data=data, language="ko-KR")