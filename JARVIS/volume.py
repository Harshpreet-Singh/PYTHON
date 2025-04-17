from urllib import request
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import time
import os
import pygame
import datetime

# for settting up audio of os 
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize Pygame mixer
pygame.mixer.init()

# Initialize pyttsx3
engine = pyttsx3.init() 
rate = engine.getProperty('rate')
engine.setProperty('rate', 155)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 for female voice

recogniser = sr.Recognizer()
newsapi = "06e53c7437cf4f2a9023e5db6e032f42"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.save_to_file(text, 'test.mp3')
    engine.runAndWait()

# Set system volume

def set_system_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(level / 100, None)

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("opening google")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("opening youtube")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com/Harshpreet-Singh")
        speak("opening your github page")
    elif "thank you jarvis" in c.lower():
        speak("Your Welcome Malik")
    elif "speak" in c.lower():
        speak("Sehaj")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
            speak(f"playing {song}")
        else:
            speak("Song not found in your library")
    elif "news" in c.lower():
        speak("I will tell you the news.")
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            titles = [article["title"] for article in articles if "title" in article]
            for title in titles[:5]:
                speak(title)
        else:
            speak("Failed to fetch news.")
    elif "volume up" in c.lower():
        try:
            current = pygame.mixer.music.get_volume() * 100
            new_vol = min(100, current + 20)
            pygame.mixer.music.set_volume(new_vol / 100)
            set_system_volume(new_vol)
            speak(f"Volume increased to {int(new_vol)} percent")
        except Exception as e:
            speak("Sorry, I couldn't increase the volume")
            print(f"Volume Up Error: {e}")
    elif "volume down" in c.lower():
        try:
            current = pygame.mixer.music.get_volume() * 100
            new_vol = max(0, current - 5)
            pygame.mixer.music.set_volume(new_vol / 100)
            set_system_volume(new_vol)
            speak(f"Volume decreased to {int(new_vol)} percent")
            print(f"Volume decreased to {int(new_vol)} percent")
        except Exception as e:
            speak("Sorry, I couldn't decrease the volume")
            print(f"Volume Down Error: {e}")
    elif "set volume to" in c.lower():
        import re
        vol_match = re.search(r"\d+", c)
        if vol_match:
            vol = int(vol_match.group())
            vol = max(0, min(100, vol))
            set_system_volume(vol)
            pygame.mixer.music.set_volume(vol / 100)
            speak(f"Volume set to {vol} percent")
    elif "mute" in c.lower():
        pygame.mixer.music.set_volume(0)
        set_system_volume(0)
        speak("Audio muted")

def main():
    speak("Initializing Jarvis... ")
    while True:
        r = sr.Recognizer()
        print("Recognizing.... ")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yeah")
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except sr.UnknownValueError:
            print("Jarvis could not understand audio! Speak Again!")
        except Exception as e:
            print("Error; {0}".format(e))

if __name__ == "__main__":
    main()
