import pandas as pd 
from google_trans_new import google_translator  
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
translator = google_translator()  
translate_text = translator.translate('Hello, I am Aadish', lang_src='en', lang_tgt='ur')  
print(translate_text)
engine.say(translate_text)
engine.runAndWait()