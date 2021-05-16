from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyttsx3
import time
import platform
plat = platform.platform()
engine = pyttsx3.init()
query = input()
if "Linux" in plat:
    PATH = "./chromedriver"
if "Windows" in plat:
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    PATH = "./chromedriver.exe"

chromeOptions = Options()
chromeOptions.headless = True
driver = webdriver.Chrome(executable_path=PATH, options=chromeOptions)

driver.get("https://www.google.com/search?q="+query)
time.sleep(2)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "wp-tabs-container"))
    )
finally:
	try:
	    element = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, "//*[@id=\"kp-wp-tab-overview\"]/div[1]/div/div/div/div/div[1]/div/div/div/span[1]"))
	    )
	finally:
		print(element.text)
		engine.say(element.text)
engine.runAndWait()
driver.close()

print("DONE NOW BYE")