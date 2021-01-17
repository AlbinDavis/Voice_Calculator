
import speech_recognition as sr
import pyttsx3


listener = sr.Recognizer()
engine = pyttsx3.init()


# talk
def talk(text):
    engine.say(text)
    engine.runAndWait()

# speech recognizing


def listen_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)
    try:
        info = r.recognize_google(audio)
        print(info)
        return info.lower()
    except Exception as e:
        print(e)


