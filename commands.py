from datetime import *

import os
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

class commands:
    def __init__(self):
        self.running = True
        self.sleep = False
        self.date = str(date.today())
        self.dirs = os.listdir()
        self.note_t = 0
        if self.date in self.dirs:
            pass
        else:
            with open(self.date, "w+") as f:
                f.write("Today's Notes")

    def say(self, text):
        engine.say(text)
        engine.runAndWait()

    def hi(self, text):
        if "hello" in text:
            self.say("Hello There, what can i do for you?\n")

    def exit(self, text):
        if "exit" in text:
            self.say("Exiting the program\n")
            self.running = False

    def note(self, text):
        if "note" in text and "write" in text:
            self.note_t+=1
            print("Taking you to noting MODE")
            self.say("Please say the notes")
            r = sr.Recognizer()
            # to close the mic after listening
            with sr.Microphone() as mic:
                r.adjust_for_ambient_noise(mic)
                print("Listening for notes...\n")
                # listening the sudden change in amplitude in the voice input
                audio = r.listen(mic)
                # var for string of audio
                said = ""
                # update for progress
                print("Recognizing the note\n")
                # in case error
                try:
                    # synthesizing the raw audio
                    said = r.recognize_google(audio)
                    print("You said", said)

                # Exception
                except Exception as e:
                    print("Exception", str(e))

            if said == "cancel" or said == "exit":
                self.say("Cacelled the noting")
            else:
                with open(self.date, "a") as f:
                    f.write("\n")
                    f.write(str(self.note_t)+") "+said)

    def check_sleep(self, text):
        if "sleep with pillow" in text:
            self.sleep = True
            print("sleeping")

    def time(self, said):
        if "time" in said and "what" in said:
            print("Go check the Clock...")
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            current_time = current_time.replace(":", "_")
            self.say(current_time)

    def show_notes(self, said):
        if "show" in said and "notes" in said:
            self.say("This part is under development")
