import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import pyautogui
import psutil  


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[0].id)  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning Bhanu!")
    elif 12 <= hour < 18:
        speak("Good afternoon Bhanu!")
    else:
        speak("Good evening Bhanu!")
    speak("I am Chotu, your voice assistant. Please tell me how may I help you.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            speak("No input detected. Please try again.")
            return "None"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("I could not understand. Please say that again.")
        return "None"
    except sr.RequestError as e:
        print("Request error from Google Speech Recognition:", e)
        return "None"

    return query


def increase_volume():
    pyautogui.press("volumeup")
    speak("Volume increased")

def decrease_volume():
    pyautogui.press("volumedown")
    speak("Volume decreased")


def mute_volume():
    pyautogui.press("volumemute")
    speak("Volume muted")


def system_condition():
    usage = str(psutil.cpu_percent())
    speak(f"CPU is at {usage} percentage")
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"Boss, your system has {percentage}% battery")

    if percentage >= 80:
        speak("We have enough charge to continue.")
    elif 40 <= percentage < 80:
        speak("It would be good to plug in the charger soon.")
    else:
        speak("Battery is low, please plug in the charger to continue.")

def openApp(command):
    if "calculator" in command:
        speak("Opening calculator")
        os.startfile('C:\\Windows\\System32\\calc.exe')
    elif "notepad" in command:
        speak("Opening notepad")
        os.startfile('C:\\Windows\\System32\\notepad.exe')
    elif "paint" in command:
        speak("Opening paint")
        os.startfile('C:\\Windows\\System32\\mspaint.exe')


def closeApp(command):
    if "calculator" in command:
        speak("Closing calculator")
        os.system("taskkill /f /im calc.exe")
    elif "notepad" in command:
        speak("Closing notepad")
        os.system('taskkill /f /im notepad.exe')
    elif "paint" in command:
        speak("Closing paint")
        os.system('taskkill /f /im mspaint.exe')


def give_schedule():
    today_schedule = """
    9:00 AM - Breakfast
    10:00 AM - Work on projects
    12:00 PM - Meeting with team
    1:00 PM - Lunch
    3:00 PM - Continue project work
    6:00 PM - Exercise
    8:00 PM - Dinner
    9:00 PM - Relax and unwind
    """
    speak("Here is your schedule for today:")
    print(today_schedule)
    speak(today_schedule)


if __name__ == "__main__":
    wishMe()
    
    while True:  
        query = takeCommand().lower()

        if query == "none":
            pass
        elif 'shutdown' in query:
            speak("Thank you for using me, Bhanu. Have a great day!")
            break  
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception:
                speak("Sorry, I couldn't find anything on Wikipedia.")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'play music' in query:
            music_dir = 'F:\\mymusic'
            if os.path.exists(music_dir):
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                else:
                    speak("No songs found in the music directory.")
            else:
                speak("Music directory not found.")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codepath = "C:\\Users\\BHANU\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            if os.path.exists(codepath):
                os.startfile(codepath)
            else:
                speak("VS Code path not found.")
        elif 'search' in query:  
            query = query.replace("search", "")  
            speak(f"Searching for {query} on Google")
            webbrowser.open(f"https://www.google.com/search?q={query}")  
        elif 'volume up' in query or 'increase volume' in query:
            increase_volume()
        elif 'volume down' in query or 'decrease volume' in query:
            decrease_volume()
        elif 'mute' in query or 'mute the volume' in query:
            mute_volume()
        elif 'system condition' in query or 'condition of the system' in query:
            system_condition()
        elif 'open calculator' in query:
            openApp(query)
        elif 'open notepad' in query:
            openApp(query)
        elif 'open paint' in query:
            openApp(query)
        elif 'close calculator' in query:
            closeApp(query)
        elif 'close notepad' in query:
            closeApp(query)
        elif 'close paint' in query:
            closeApp(query)
        elif 'today schedule' in query or 'schedule of today' in query:
            give_schedule()
        else:
            speak("I didn't understand that. Please say it again.")
