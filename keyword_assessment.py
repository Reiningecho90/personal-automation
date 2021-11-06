import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

with mic as source:
    r.adjust_for_ambient_noise(source)

    while True:
        print('speak now')

        audio = r.listen(mic)
        audio = r.recognize_google(audio)

        print(audio)