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
            with open("./NoteNumber/"+self.date, "r") as f:
                self.note_t = int(f.read())
                print(self.note_t)
        else:

            with open(self.date, "w+") as f:
                f.write("Today's Notes")
            os.chdir("./NoteNumber")
            print(os.curdir)
            with open(self.date, "w+") as f:
                f.write("0")
            os.chdir("..")

    def say(self, text):
        engine.say(text)
        engine.runAndWait()

    def name(self, text):
        if "what" in text and "name" in text:
            self.say("My name is lolo")

    def how(self, text):
        if "how" in text and "you" in text and "are" in text:
            self.say("I am fit and fine, what can I do for you")

    def hi(self, text):
        if "hello" in text:
            self.say("Hello There, what can i do for you?\n")

    def exit(self, text):
        if "exit" in text:
            self.say("Exiting the program\n")
            self.running = False
            os.chdir("./NoteNumber")
            with open(self.date, "w+") as f:
                f.write(str(self.note_t))
            os.chdir("..")

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
                    self.say("Saved the file")

    def check_sleep(self, text):
        if "go to sleep" in text:
            self.sleep = True
            self.say("Went to sleep mode")
            while self.sleep:
                r = sr.Recognizer()
                with sr.Microphone() as mic:
                    r.adjust_for_ambient_noise(mic)
                    print("Waiting for the Wake Up Command\n")
                    audio = r.listen(mic)
                    said = ""
                    print("Recognizing\n")
                    try:
                        said = r.recognize_google(audio)
                        print(said)

                    except Exception as e:
                        print("Exception", str(e))
                
                if "get up" in said:
                    self.sleep = False
                    self.say("Welcome back sir")
                else:
                    self.sleep = True

    def time(self, said):
        if "time" in said and "what" in said:
            print("Go check the Clock...")
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            current_time = current_time.replace(":", "_")
            self.say(current_time)

    def show_notes(self, said):
        if "tell" in said and "notes" in said:
            self.say("Under Development")

    def tell_age(self, said):
        if "age" in said and "what" in said:
            self.say("My age is hundred years")