from urllib import request
import speech_recognition as sr # speech to text convert and recognize
import pyttsx3 # for audio recognition
import webbrowser # for opening url in default web browser
import musicLibrary # this is my generated file
import requests # to request news and open ai
import openai # to access open ai's api
import os # for accessing system
import re # for volume adjustment
import time 
import datetime # for use of date and time
# use PYGAME for gTTS or ANY OTHER otherwise don't import 
import pygame
import pyautogui
pyautogui.FAILSAFE = False # now click will not stop
from gtts import gTTS
# import cv2 # to capture camera
import pygame.camera
from pygame.locals import *
# setting up notification push
# from win10toast import ToastNotifier
# win10toast is only for win10 so using plyer is better option
from plyer import notification
from win10toast_click import ToastNotifier
import threading
import winotify  # alternate option for notifications
# for settting up audio of os 
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# for opening applications/ softwares installed in system
import pygetwindow as gw
import win32gui
import win32con
import pyperclip # used to copy text to clip board
import subprocess # using for screen saver

# Initialize Pygame mixer (MUST be done first)
pygame.mixer.init()

# level: 0-100
def set_system_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(level/100, None)

# MAKING CHANGES IN PYTTSX3
engine = pyttsx3.init() 
engine = pyttsx3.init() 
rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
engine.setProperty('rate', 155)     # setting up new voice rate

voices = engine.getProperty('voices')       #getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

recogniser = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "your_key_here"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.save_to_file(text, 'test.mp3')
    engine.runAndWait()

# _________________PAID HAI gTTS__________________
# def speak_paid(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3')
#     # Initialize pygame mixer
#     pygame.mixer.init()

#     # Load a sound file
#     pygame.mixer.music.load('temp.mp3')

#     # play the mp3 file
#     pygame.mixer.music.play()

#     # keep the program running until the music stops playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)

#     pygame.mixer.music.unload()
#     os.remove("temp.mp3")

#  _____________________PAID HAI OPEN AI_____________________
# def aiProcess(command):
#     client = openai.OpenAI(api_key="your_key_here")
#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant Jarvis, skilled in general tasks like alexa and google"},
#         {"role": "user", "content": command}
#     ]
#     )
#     return completion.choices[0].message.content

# screensaver
def activate_screensaver():
    subprocess.run(["C:\\Windows\\System32\\scrnsave.scr", "/s"])

# OPENING SYSTEM APPS
# >> MAP YOUR APPLICATIONS HERE
app_paths = {
                    "notepad": "notepad.exe",
                    "calculator": "calc.exe",
                    "google": "chrome.exe",
                    "word": "winword.exe",
                    "excel": "excel.exe",
                    "studio": "Code.exe",
                    "this pc": "shell:MyComputerFolder",
                    "desktop": "shell:Desktop"
                    # Add more apps and their paths here
}
def focus_or_open_app(app_name):
    # First try to switch to the app if it's already open
    windows = gw.getWindowsWithTitle(app_name.capitalize())
    if windows:
        window = windows[0]
        if not window.isActive:
            win32gui.ShowWindow(window._hWnd, win32con.SW_RESTORE)  # Restore if minimized
            win32gui.SetForegroundWindow(window._hWnd)
            speak(f"Switched to {app_name}")
        else:
            speak(f"{app_name} is already active.")
    else:
        # If not found, try opening the app
        if app_name in app_paths:
            try:
                os.startfile(app_paths[app_name])
                speak(f"Opening {app_name}")
            except Exception as e:
                speak(f"Sorry, I couldn't open {app_name}")
                print(e)
        else:
            speak("Application not found in my database.")

#  capture camera 
def capture_image():
    # Initialize pygame and its camera module
    pygame.init()
    pygame.camera.init()
    # Get list of available cameras
    camlist = pygame.camera.list_cameras()
    if not camlist:
        print("No camera found!")
        speak("No camera found!")
        return
    # Start the first available camera
    cam = pygame.camera.Camera(camlist[0], (640, 480))
    cam.start()
    # Allow camera to warm up
    time.sleep(1)
    # Capture image
    image = cam.get_image()
    # Save image
    file_name = f"captured_{int(time.time())}.jpg"
    pygame.image.save(image, file_name)
    print(f"Image saved as {file_name}")
    cam.stop()

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
    elif "thank you" in c.lower():
        speak("Your Welcome Malik")
    elif "speak" in c.lower():
        speak("Gal sun lallaria ve Ah lok mere te hasde Paise jyada dedugi Matching krdega ta dsde Sunla ve dito same chahidi Ah le photo ve Ferrari laal di")
    elif "open terminal" in c.lower():
        pyautogui.hotkey('ctrl', '`')
    elif "open insta" in c.lower() or "open instagram" in c.lower():
        speak("opening instagram")
        webbrowser.open("htttps://instagram.com/harshpreet170607")
# OPENING SYSTEM APPS CONTINUED HERE
    elif "open app" in c.lower() or "open application" in c.lower() or "open" in c.lower():
            speak("Which application should I open or switch to?")
            try:
                with sr.Microphone() as source:
                    audio = recogniser.listen(source, timeout=5)
                    app_name = recogniser.recognize_google(audio).lower().strip()
                    focus_or_open_app(app_name)
            except Exception as e:
                speak("Sorry, I couldn't understand the application name.")
                print(e)

# SHOWING DESKTOP
    elif "show desktop" in c.lower() or "open desktop screen" in c.lower():
        speak("Showing desktop")
        pyautogui.hotkey('win', 'd') # this controlls keyboard bro

# REFRESHING PAGE OR RELOADING PAGE
    elif "refresh" in c.lower() or "reload" in c.lower():
        speak("Refreshing..")
        pyautogui.hotkey('f5') # this controlls keyboard bro

# CAPTURE CAMERA IMAGE
    elif "take picture" in c.lower() or "capture image" in c.lower():
        speak("Capturing image now.")
        capture_image()
        speak("Image captured and saved.")

# Applying screensaver
    elif "screensaver" in c.lower():
        speak("Turning on the screen saver.")
        activate_screensaver()

# (_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_) CURSOR CLICK (_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)
    elif "use mouse" in c.lower():
        speak("Where should I click? You can say center, top left, top right, or custom.")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            position_command = r.recognize_google(audio).lower()
            print(f"You said: {position_command}")
            x, y = None, None  # Initialize to avoid "unbound variable" error
            if "centre" in position_command or "center" in position_command:
                screen_width, screen_height = pyautogui.size()
                x, y = screen_width // 2, screen_height // 2
            elif "top left" in position_command:
                x, y = 0, 0
            elif "top right" in position_command:
                screen_width, screen_height = pyautogui.size()
                x, y = screen_width - 1, 0
            elif "custom" in position_command:
                speak("Say X coordinate")
                with sr.Microphone() as source:
                    audio = r.listen(source)
                try:
                    x = int(r.recognize_google(audio).lower())
                except:
                    speak("Couldn't understand the X coordinate.")
                    return
                speak("Say Y coordinate")
                with sr.Microphone() as source:
                    audio = r.listen(source)
                try:
                    y = int(r.recognize_google(audio).lower())
                except:
                    speak("Couldn't understand the Y coordinate.")
                    return
            if x is not None and y is not None:
                speak(f"Clicking at {x}, {y}")
                pyautogui.moveTo(x, y)
                pyautogui.mouseDown()
                pyautogui.mouseUp()
            else:
                speak("Invalid position specified.")
        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, I couldn't understand where to click.")
# minimize
    # elif "minimize" in c.lower() or "small" in c.lower() or "window down" in c.lower() or "down" in c.lower():
    #     try:
    #         speak("Minimizing Now..")
    #         pyautogui.click(1260, 14)
    #     except Exception as e:
    #         speak("Can't click")
    
# NOTIFACTIONS BELLOW

# (_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_) FOLLOWING IS WIN10TOAST (_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)
    # elif "notify" in c.lower():
    #     def windows_notification(title, message):
    #         toaster = ToastNotifier()
    #         toaster.show_toast(
    #             title,
    #             message,
    #             icon_path=None,
    #             duration=5,
    #             threaded=True
    #         )
    #     windows_notification("JARVIS Alert", "New email received!")

# (_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_) FOLLOWING IS PLYER (_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)

# CUSTOM NOTIFICTION
    elif "send me" in c.lower():
        speak("trying..")
        def show_notification():
                    notification.notify(
                        title='JARVIS',
                        message='NO HAPPINESS FOUND 🙁',
                        app_name='JARVIS Assistant',
                        app_icon='jarvis.ico',
                        timeout=8  # Notification duration in seconds
                    )
        show_notification()
# SPEAK TIME
    elif "tell time" in c.lower():
    # elif "tell time" in command.lower() or "tell date" in c.lower() or "what is time" in c.lower() or "what is date" in c.lower():
        # try:
            now = datetime.datetime.now()
            # Time in 12-hour format with AM/PM
            current_time = now.strftime("%I:%M %p")  # e.g., "02:30 PM"
            # Date in friendly format
            current_date = now.strftime("%A, %B %d, %Y")
            # Speak both
            print(f"The time is {current_time} on {current_date}")
            # Show notification
            notification.notify(
                title='JARVIS - Time and Date',
                message=f"{current_time}\n{current_date}",
                app_name='JARVIS Assistant',
                app_icon='jarvis.ico',  # Optional icon
                timeout=10
            )
        # except Exception as e:
        #     print("Sorry, I couldn't check the time and date")
        #     print(f"Time/date error: {e}")

# clickable notification
    elif "notify" in c.lower():
        speak("Preparing clickable notification")
        try:
            def open_url():
                webbrowser.open("https://google.com")
                speak("Opening Google in your browser")
            def show_notification():
                toaster = ToastNotifier()
                toaster.show_toast(
                    "JARVIS Assistant",
                    "Click here to open Google",
                    icon_path="jarvis.ico",  # Custom icon
                    duration=15,
                    threaded=False,  # Changed for better reliability
                    callback_on_click=open_url
                )
            # Run in a thread to avoid blocking
            notif_thread = threading.Thread(target=show_notification)
            notif_thread.start()
            speak("Notification sent. Click it to activate.")
        except ImportError:
            speak("Notification feature not available")
        except Exception as e:
            print(f"Error: {e}")
            speak("Couldn't create clickable notification")
    # elif "click" in c.lower():
    #     def callback():
    #         webbrowser.open("https://google.com")

    #         toaster = ToastNotifier()
    #         toaster.show_toast(
    #             "Click Me",
    #             "Notification with action",
                # callback_on_click=callback
            # )


# MUSIC BELOW   
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
# FETCH NEWS
    elif "news" in c.lower():
        speak("I will tell you the news.")
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            titles = [article["title"] for article in articles if "title" in article]
            
            for title in titles[:5]:  # Speak top 5 headlines
                speak(title)
        else:
            speak("Failed to fetch news.")
    # else:
    #     # let OpenAi handle the requests
    #     output = aiProcess(c)
    #     speak(output)

    elif "set volume to" in c.lower():
        vol_match = re.search(r"\d+", c)
        if vol_match:
            vol = int(vol_match.group())
            vol = max(0, min(100, vol))
            set_system_volume(vol)
            pygame.mixer.music.set_volume(vol / 100)
            speak(f"Volume set to {vol} percent")    
    # Mute/Unmute

    elif "mute" in c.lower():
        pygame.mixer.music.set_volume(0)
        set_system_volume(0)
        print("Audio muted")
    # else:
    #     speak("failed to mute")
          
    # Take screenshot
    elif "take screenshot" in c.lower() or "capture screen" in c.lower() or "screenshot" in c.lower():
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshots\\screenshot_{now}.jpg"
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        # speak(f"Screenshot saved as {filename}")
        speak(f"Screenshot saved")
    

if __name__ == "__main__":
    speak("Initializing Jarvis... ")
    while True:
        # LISTEN FOR THE WAKE WORD "JARVIS"
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("Recognizing.... ")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            # recognize speech using google
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yeah  ")
                # LISTEN FOR THE COMMAND 
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    # speak("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


            elif(word.lower() == "exit" or word.lower() == "quit"):
                print("Goodbye!")
                speak("Goodbye!")
                def show_notification():
                    notification.notify(
                        title='JARVIS',
                        message='Good Bye! USE ME AGAIN',
                        app_name='JARVIS Assistant',
                        app_icon='jarvis.ico',
                        timeout=8  # Notification duration in seconds
                    )
                show_notification()
                break
        except sr.UnknownValueError:
            print("Jarvis could not understand audio! Speak Again!")
        except Exception as e:
            print("Error; {0}".format(e))