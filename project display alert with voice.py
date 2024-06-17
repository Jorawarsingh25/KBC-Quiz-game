from plyer import notification
import time
from gtts import gTTS
import os

# Function to speak the message
def speak(message):
    tts = gTTS(text=message, lang='en')
    tts.save("notification.mp3")
    os.system("start notification.mp3")

while True:
    notification.notify(title="Hello", message="Hello Jorawar!", timeout=2)
    speak("Hello Jorawar!")  # Speak the message
    time.sleep(5)
