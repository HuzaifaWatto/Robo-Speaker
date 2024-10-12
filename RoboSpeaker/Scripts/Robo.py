import os
import win32com.client

while True:
    x=input(f"Enter the word you want say: ")
    if x == 'q':
        speaker.Speak("bye bye friend")
        break
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(x )
