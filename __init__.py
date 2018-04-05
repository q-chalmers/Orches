#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from time import ctime
import time
import os
import webbrowser
from gtts import gTTS
from pygame import mixer as mixer


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    mixer.init()
    mixer.music.load("audio.mp3")
    mixer.music.play()
    #pauses program to give the bot time to speak
    while mixer.music.get_busy():
        pass
    mixer.music.stop()
    tts.save("placeHolderFile.mp3")
    mixer.music.load("placeHolderFile.mp3")
    os.remove("audio.mp3")


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def aI(data):
    if "how are you" in data:
        speak("I am fine")

    if "thats all" in data:
        speak("Ok, Goodbye")
        SystemExit()

    if "what time is it" or "what is the time" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = ""
        for i in range(2, len(data)):
            location = location + data[i]
        speak("Hold on, I will show you where " + location + " is.")
        #need to make it so the array of data extends to everything after the is
        webbrowser.open_new("https://www.google.nl/maps/place/" + location + "/&amp;")

    if ("what is" or "search for") in data:
        data = data.split(" ")
        search = data[2]
        speak("here is what i found for"+ search)
        webbrowser.open_new(search)
        #just changes this. it isnt tested but proably wont work.
        webbrowser.open_new(search)

    if ("what are you counting down") in data:
        speak("the time before i am smart enough to replace you")

# initialization
time.sleep(2)
speak("Hello, I am Orchus")
speak("What do you need?")
while 1:
    data = recordAudio()
    aI(data)
