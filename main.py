import pyttsx3
import speech_recognition as sr
from commands import commands

engine = pyttsx3.init()

# properties
engine.setProperty('rate', 145)
engine.setProperty('volume', 1)
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_MarkM"
engine.setProperty('voice', voice_id)

# requirements
c = commands()
c.say("Hello, I am lolo. I am your personal voice assistant")

while c.running:
    # variable for recognizing
    r = sr.Recognizer()
    # to close the mic after listening
    with sr.Microphone() as mic:
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
            # giving out the synthesized audio
            c.hi(said)

            c.exit(said)

            c.note(said)

            print(said)
            print("finished the cases, now restarting")
        # Exception
        except Exception as e:
            print("Exception", str(e))

c.say("Have a good day sir")
