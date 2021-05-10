# rquirements
import pyttsx3
import speech_recognition as sr
from selenium import webdriver
from commands import commands, base_functions

engine = pyttsx3.init()

# properties
engine.setProperty('rate', 145)
engine.setProperty('volume', 1)

# requirements-
c = commands()
base = base_functions()
base.say("Hello, I am lolo. I am your personal voice assistant")

while c.running:
    # variable for recognizing
    r = sr.Recognizer()
    # to close the mic after listening
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic)
        print("Listening for Input...\n")
        # listening the sudden change in amplitude in the voice input
        audio = r.listen(mic)
        # var for string of audio
        said = ""
        # update for progress
        print("Recognizing the input\n")
        # in case error
        try:
            # synthesizing the raw audio
            said = r.recognize_google(audio)
            print("You said", said)
            # giving out the synthesized audio
            c.hi(said)

            c.name(said)

            c.how(said)

            c.exit(said)

            c.note(said)

            c.time(said)

            c.show_notes(said)

            c.check_sleep(said)

            c.tell_age(said)

            print("finished the cases, now restarting")
        # Exception
        except Exception as e:
            print("Exception", str(e))
            base.say("Could not understand the speech, give it another try")

base.say("Have a good day sir")
