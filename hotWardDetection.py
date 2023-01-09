import os
import speech_recognition as sr




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
                takeCommand()
                # return -1

        return query.lower()


while True:
    
    
    wake_up = takeCommand()
    
    if 'wake up' in wake_up:
        os.startfile('D:\\Self-Work\\jarvis\\jarvis.py')
        
    else:
        print('Nothing.........')