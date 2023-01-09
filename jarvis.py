import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import wikipedia
from datetime import datetime
import pyautogui
# import geocoder
import keyboard
import pyjokes
import bs4
from pydictionary import Dictionary



Assistant = pyttsx3.init("sapi5")
voices = Assistant.getProperty("voices")
# print(voices)
Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate', 170)


def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f"Jarvis : {audio}")
    print("   ")
    Assistant.runAndWait()

def takeCommand():
        global query
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.........")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing..........")
                query = command.recognize_google(audio,language='en-in').lower()
                print(f"You said :  {query}" )
                # return query.lower()
            except Exception as Error:
                # print("Say it again")
                Speak("Sorry! Say it again ")
                takeCommand()
                # return -1

        return query.lower()

# # query = takeCommand()

# Speak("Hello !, Snehal sir, I'm Your Jarvis!, How can i help you")
# # takeCommand()

def TaskExe():

    Speak("Welcome Sir, I am Jaarvush .")
    Speak("How Can I Help You ?")

    def Music(musicName):
        Speak("Sir , Tell me the name of song!")
        # musicName = takeCommand()
        # musicName = query.replace("hey jarvis","")
        # musicName = query.replace("please","")
        if 'uncharted' in musicName:
                os.startfile('D:\\Movies\\Uncharted.mp4')
        else:
            pywhatkit.playonyt(musicName)


    def Whatsapp():
        Speak("Tell me the name of person!")
        name = takeCommand()

        if 'shreya' in name or 'pallavi' in name or 'girlfriend' in name:
            Speak("Sir, I'm sending Message To Shreya ! Please Tell me the Message!")
            msg = takeCommand()
            # time = takeCommand()
            Speak("Tell me the time hours Sir!")
            # Speak("TIme In Hours!")
            hour = int(takeCommand())
            Speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg('+919142995706', msg,hour,min,20)
            Speak(f"Sir, Sending Whatsapp Message to {name} !")
        elif 'papa' in name:
                Speak("Tell me the Message!")
                msg = takeCommand()
                Speak("Tell me the time hours Sir!")
                # Speak("TIme In Hours!")
                hour = int(takeCommand())
                Speak("Time in minutes!")
                min = int(takeCommand())
                pywhatkit.sendwhatmsg('+918409961282', msg,hour,min,20)
                Speak(f"Sir, Sending Whatsapp Message to {name} !")
        else:
            Speak("Sir, Contact not found!")             
            Speak("Tell me the phone Number !")
            phone = int(takeCommand())
            ph = '+91'+phone
            Speak("Tell me the Message !")
            msg = takeCommand()
            Speak("Tell me the time Sir!")
            Speak("TIme In Hours!")
            hour = int(takeCommand())
            Speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg(ph, msg,hour,min,20)
            Speak("Sir, Sending Whatsapp Message !")

    def OpenApps():
        Speak("Ok Sir!, Wait a second")

    ############ Currently only vs code will open  
        if 'code' in query:
            os.startfile("C:\\Users\ACER\AppData\Local\Programs\Microsoft VS Code\Code.exe")   
        elif 'telegram' in query:
            os.startfile("C:\\Users\ACER\AppData\Local\Programs\Microsoft VS Code\Code.exe")   
        elif 'whatsapp' in query:
            os.startfile("C:\\Users\ACER\AppData\Local\Programs\Microsoft VS Code\Code.exe")   
        elif 'chorme' in query:
            os.startfile('"C:\\Program Files\Google\Chrome\Application\chrome.exe"')   
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')
        elif 'map' in query:
            webbrowser.open('https://www.google.co.in/maps/place/Chandigarh/@30.7352102,76.6934891')
            Speak("Here it is sir")

    def CloseApps():
        Speak("Ok Sir, Wait a second !")

        if 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")
        elif 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")
        elif 'code' in query:
            os.system("TASKKILL /F /im Code.exe")
        elif 'facebook' in query:
            os.system("TASKKILL /F /im chrome.exe")
        elif 'map' in query:
            os.system("TASKKILL /F /im chrome.exe")

        Speak("Your Application has been sucessfully closed")

    def YoutubeAuto():
        Speak("Whats your Command ?")
        comm = takeCommand()

        if 'pause' in comm:
            keyboard.press('space-bar')
        elif 'restart' in comm:
            keyboard.press('0')
        elif 'mute' in comm:
            keyboard.press('m')
        elif 'skip' in comm:
            keyboard.press('l')
        elif 'back' in comm:
            keyboard.press('j')
        elif 'full screen' in comm:
            keyboard.press('f')
        elif 'film mode' in comm:
            keyboard.press('t')

        Speak("Done Sir")

    def ChromeAuto():
        Speak("Chrome Automation started!")

        commmand = takeCommand()

        if 'close this tab' in commmand:
            keyboard.press_and_release('ctrl + w')
        elif 'open new tab' in commmand:
            keyboard.press_and_release('ctrl + t')
        elif 'open new window' in commmand:
            keyboard.press_and_release('ctrl + n')
        elif 'history' in commmand:
            keyboard.press_and_release('ctrl + h')
        elif 'download' in commmand:
            keyboard.press_and_release('ctrl + j')
        elif 'history' in commmand:
            keyboard.press_and_release('ctrl + h')

    def Dict():
        Speak("Activated Dictinary!")
        Speak("Tell me the Problem!")
        prob1 = takeCommand()

        if 'meaning' in prob1:
            prob1 = prob1.replace("what is the", "")
            prob1 = prob1.replace("jarvis", "")
            prob1 = prob1.replace("of", "")
            prob1 = prob1.replace("meaning", "")
            dict = Dictionary(prob1,10)
            result = dict.meanings()
            Speak(f"The Meaning of {prob1} is {result}")

    def ScreenShot():
        Speak("Ok Sir, What should i name that file ?")
        path = takeCommand()
        fileName = path +".png"
        dir = "D:\\\Self-Work\\jarvis\\screenshots\\"+fileName
        ss = pyautogui.screenshot()
        ss.save(dir)
        os.startfile("D:\\\Self-Work\\jarvis\\screenshots")
        Speak("Here is Your Screenshot")

    while True:

        query = takeCommand()

        if 'hello' in query or 'hi' in query:
            Speak("Hello Sir, I am Jarvis .")
            Speak("How may i help you?")
        elif 'how are you' in query:
            Speak("I am fine Sir!")
            Speak("What about YOU?")
        elif 'bye' in query or 'good night' in query or 'see you' in query:
            Speak("Sure sir, You can call me AnyTime !")
            Speak("Just Say Wake Up")
            break
        elif 'search' in query:
            if 'youtube' in query:
                Speak("Ok Sir, THis is what i found for your search !")
                query = query.replace("jarvis","")
                query = query.replace("search in youtube","")
                web = 'https://www.youtube.com/results?search_query=' + query
                webbrowser.open
                Speak("Done Sir")
            elif 'google' in query:
                Speak("Ok Sir, THis is what i found for your search !")
                query = query.replace("jarvis","")
                query = query.replace("search in google ","")
                web = 'https://www.youtube.com/results?search_query=' + query
                webbrowser.open
                # pywhatkit.search(query)
                Speak("Done Sir")
        elif 'website' in query:
             Speak("Ok Sir, Launching........")
             query = query.replace("jarvis","")
             query = query.replace("website","")
             query = query.replace(" ","")
             domain = query.replace("open","")
             websiteOpen = 'https://wwww.'+ domain + '.com'
             webbrowser.open(websiteOpen)
             Speak("Sir ! "+domain+" has been launched, here you can view it !")
        elif 'launch' in query:
            Speak("Yes Sir, Tell me, Which website you want to open ?")
            name = takeCommand()
            websiteOpen = 'https://wwww.'+ name + '.com'
            webbrowser.open(web)
            Speak("Done Sir !")
        elif 'music' in query:
            # if 'play the music' in query:
            Speak("Yes Sir, Tell me, Which song you want to listen?")

            musicName = takeCommand()
            Music(musicName)
## https://youtu.be/eLU4ZsoJleg?list=PLkjZS1KzvTGEfpDzt7iTNboJiWtxqS9JE&t=981

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia......")
            query = query.replace('jarvis','')
            query = query.replace('wikipedia','')
            print(query)
            wiki = wikipedia.summary(query,sentences = 2)

            htmlDoc = bs4.BeautifulSoup(wiki, "lxml")
            print(htmlDoc)
            # Speak(htmlDoc)
           
            Speak(f"According to wikipedia : {wiki}")
        elif 'whatsapp message' in query:
            Whatsapp()
        elif 'screenshot' in query:
            ScreenShot()
        elif 'open facebook' in query:
            OpenApps()
        elif 'open youtube' in query:
            OpenApps()
        elif 'code' in query:
            OpenApps()
        elif 'open whatsapp' in query:
            OpenApps()
        elif 'open chorme' in query:
            OpenApps()
        elif 'open map' in query:
            OpenApps()
        elif 'close facebook' in query:
            CloseApps()
        elif 'close map' in query:
            CloseApps()
        elif 'close whatsapp' in query:
            CloseApps()
        elif 'close code' in query:
            CloseApps()
        elif 'pause' in query:
            keyboard.press('space-bar')
        elif 'restart' in query:
            keyboard.press('0')
        elif 'mute' in query:
            keyboard.press('m')
        elif 'skip' in query:
            keyboard.press('l')
        elif 'back' in query:
            keyboard.press('j')
        elif 'full screen' in query:
            keyboard.press('f')
        elif 'film mode' in query:
            keyboard.press('t')
        elif 'film mode' in query:
            keyboard.press('t')
        elif 'youtube tool' in query:
            YoutubeAuto()         
        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')
        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
        elif 'download' in query:
            keyboard.press_and_release('ctrl + j')
        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
        elif 'chrome automation' in query:
            ChromeAuto()
        elif 'joke' in query:
            getJoke = pyjokes.get_joke(language="en", category="neutral")
            Speak(getJoke)
        elif 'repeat my words' in query:
            Speak("Speak Sir!")
            myWords = takeCommand()
            Speak(f"You Said : {myWords}")
        elif 'dictionary' in query:
            Dict()
        elif 'girlfriend name' in query:
            Speak("Sir, Which one  ")
            Speak("Pikachu , Shreya , Pallavi ?")
        else:
            Speak("I have not authority to do that Sir")


   
TaskExe()
        