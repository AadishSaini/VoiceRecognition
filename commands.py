import pyttsx3
from datetime import datetime
import speech_recognition as sr

engine = pyttsx3.init()

class commands:
    def __init__(self):
        self.running = True
        self.sleep = False

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
        if "note that" or "remember that" or "note" in text:
            print("Taking you to noting MODE")
            r = sr.Recognizer()
            with sr.Microphone() as mic:
                self.say("Please say whatever you want to save")
                print("Listening in noting mode")
                audio = r.listen(mic)
                said = ""
                try:
                    print("recognizing in noting mode")
                    said = r.recognize_google(audio)
                    if "exit" == said:
                        self.running = False
                except Exception as e:
                    print("Noting error", str(e))

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            current_time = current_time.replace(":", "_")
            with open(current_time, 'w+') as f:
                f.write(said)

            self.say("Saved the file")
            print("Came out of noting mode")

    def sleep(self, text):
        if "sleep with pillow" in text:
            self.sleep = True
            print("sleeping")
