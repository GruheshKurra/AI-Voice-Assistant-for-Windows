import speech_recognition as sr
import pyttsx3
import os
import subprocess
import webbrowser
import psutil
import pyautogui
import ctypes
import shutil
from pynput.keyboard import Key, Controller
from pywinauto.application import Application

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "female" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return command.lower()

def greet_user():
    speak("Hi Karthik, I am AI Assistant. How can I assist you today?")

# System and Application Functions
def open_file_explorer():
    speak("Opening File Explorer")
    os.startfile("explorer.exe")

def close_chrome():
    speak("Closing Chrome")
    os.system("taskkill /im chrome.exe /f")

def minimize_chrome():
    speak("Minimizing Chrome")
    app = Application().connect(path="chrome.exe")
    app.Chrome.minimize()

def minimize_all_windows():
    speak("Minimizing all windows")
    pyautogui.hotkey('win', 'd')

def shutdown():
    speak("Shutting down the computer")
    os.system("shutdown /s /t 1")

def restart():
    speak("Restarting the computer")
    os.system("shutdown /r /t 1")

def open_notepad():
    speak("Opening Notepad")
    os.system("notepad.exe")

def open_calculator():
    speak("Opening Calculator")
    os.system("calc.exe")

def perform_calculation(calculation):
    speak(f"Performing calculation: {calculation}")
    os.system(f"calc.exe")
    time.sleep(2)
    keyboard = Controller()
    keyboard.type(calculation)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def open_browser():
    speak("Opening Browser")
    webbrowser.open("http://www.google.com")

def open_chrome(url=None):
    speak("Opening Google Chrome")
    if url:
        webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(url)
    else:
        os.startfile("chrome.exe")

def play_music():
    speak("Playing music")
    # Replace with the path to your music file
    os.startfile("path_to_your_music_file.mp3")

def check_battery():
    speak("Checking battery status")
    battery = psutil.sensors_battery()
    speak(f"Battery is at {battery.percent} percent")

def lock_pc():
    speak("Locking the computer")
    os.system("rundll32.exe user32.dll,LockWorkStation")

def log_off():
    speak("Logging off")
    os.system("shutdown -l")

def open_settings():
    speak("Opening Settings")
    os.system("start ms-settings:")

def open_task_manager():
    speak("Opening Task Manager")
    os.system("taskmgr")

def navigate_to_folder(folder_name):
    paths = {
        "desktop": os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'),
        "documents": os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents'),
        "downloads": os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads'),
        "pictures": os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures'),
        "music": os.path.join(os.path.join(os.environ['USERPROFILE']), 'Music'),
        "videos": os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos')
    }
    if folder_name in paths:
        path = paths[folder_name]
        speak(f"Opening {folder_name} folder")
        os.startfile(path)
    else:
        speak(f"Folder {folder_name} not found")

def create_file(filename):
    with open(filename, 'w') as f:
        speak(f"Creating file {filename}")
        f.write("")

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        speak(f"Deleted file {filename}")
    else:
        speak(f"File {filename} not found")

def create_folder(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)
        speak(f"Created folder {foldername}")
    else:
        speak(f"Folder {foldername} already exists")

def delete_folder(foldername):
    if os.path.exists(foldername):
        shutil.rmtree(foldername)
        speak(f"Deleted folder {foldername}")
    else:
        speak(f"Folder {foldername} not found")

def open_control_panel():
    speak("Opening Control Panel")
    os.system("control")

def open_cmd():
    speak("Opening Command Prompt")
    os.system("start cmd")

def open_power_shell():
    speak("Opening PowerShell")
    os.system("start powershell")

def mute_volume():
    speak("Muting volume")
    os.system("nircmd.exe mutesysvolume 1")

def unmute_volume():
    speak("Unmuting volume")
    os.system("nircmd.exe mutesysvolume 0")

def volume_up():
    speak("Increasing volume")
    os.system("nircmd.exe changesysvolume 2000")

def volume_down():
    speak("Decreasing volume")
    os.system("nircmd.exe changesysvolume -2000")

def open_edge():
    speak("Opening Microsoft Edge")
    os.system("start msedge")

def open_word():
    speak("Opening Microsoft Word")
    os.system("start winword")

def open_excel():
    speak("Opening Microsoft Excel")
    os.system("start excel")

def open_powerpoint():
    speak("Opening Microsoft PowerPoint")
    os.system("start powerpnt")

def system_info():
    speak("Opening System Information")
    os.system("msinfo32")

def youtube_pause():
    speak("Pausing YouTube")
    pyautogui.press('space')

def youtube_play():
    speak("Playing YouTube")
    pyautogui.press('space')

def spotify_play():
    speak("Playing Spotify")
    pyautogui.press('playpause')

def spotify_pause():
    speak("Pausing Spotify")
    pyautogui.press('playpause')

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't programmers like nature? It has too many bugs."
    ]
    import random
    joke = random.choice(jokes)
    speak(joke)

def surprise_me():
    surprises = [
        "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible!",
        "A day on Venus is longer than a year on Venus. It takes Venus longer to rotate on its axis than to orbit the Sun.",
        "Bananas are berries, but strawberries aren't."
    ]
    import random
    surprise = random.choice(surprises)
    speak(surprise)

if __name__ == "__main__":
    greet_user()
    while True:
        command = take_command()

        if 'open file explorer' in command:
            open_file_explorer()
        elif 'close chrome' in command:
            close_chrome()
        elif 'minimize chrome' in command:
            minimize_chrome()
        elif 'minimise all' in command:
            minimize_all_windows()
        elif 'shutdown' in command:
            shutdown()
        elif 'restart' in command:
            restart()
        elif 'open notepad' in command:
            open_notepad()
        elif 'open calculator' in command:
            open_calculator()
        elif 'calculate' in command:
            calculation = command.replace('calculate', '').strip()
            perform_calculation(calculation)
        elif 'open browser' in command:
            open_browser()
        elif 'open chrome' in command:
            url = command.replace('open chrome', '').strip()
            if url:
                open_chrome(url)
            else:
                open_chrome()
        elif 'play music' in command:
            play_music()
        elif 'check battery' in command:
            check_battery()
        elif 'lock' in command:
            lock_pc()
        elif 'log off' in command:
            log_off()
        elif 'open settings' in command:
            open_settings()
        elif 'open task manager' in command:
            open_task_manager()
        elif 'navigate to' in command:
            folder_name = command.replace('navigate to', '').strip().lower()
            navigate_to_folder(folder_name)
        elif 'create file' in command:
            filename = command.replace('create file', '').strip()
            create_file(filename)
        elif 'delete file' in command:
            filename = command.replace('delete file', '').strip()
            delete_file(filename)
        elif 'create folder' in command:
            foldername = command.replace('create folder', '').strip()
            create_folder(foldername)
        elif 'delete folder' in command:
            foldername = command.replace('delete folder', '').strip()
            delete_folder(foldername)
        elif 'open control panel' in command:
            open_control_panel()
        elif 'open command prompt' in command:
            open_cmd()
        elif 'open powershell' in command:
            open_power_shell()
        elif 'mute volume' in command:
            mute_volume()
        elif 'unmute volume' in command:
            unmute_volume()
        elif 'volume up' in command:
            volume_up()
        elif 'volume down' in command:
            volume_down()
        elif 'open edge' in command:
            open_edge()
        elif 'open word' in command:
            open_word()
        elif 'open excel' in command:
            open_excel()
        elif 'open powerpoint' in command:
            open_powerpoint()
        elif 'system info' in command:
            system_info()
        elif 'youtube pause' in command:
            youtube_pause()
        elif 'youtube play' in command:
            youtube_play()
        elif 'spotify play' in command:
            spotify_play()
        elif 'spotify pause' in command:
            spotify_pause()
        elif 'tell me a joke' in command:
            tell_joke()
        elif 'surprise me' in command:
            surprise_me()
        elif 'stop' in command or 'exit' in command:
            speak("Exiting the assistant. Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that command.")
