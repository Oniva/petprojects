#! python 3
#  Natural Language Processing - TBD

import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio = r.listen(source)
voiceRecord = r.recognize_google(audio)
voiceLen = len(voiceRecord)
print(voiceRecord)

