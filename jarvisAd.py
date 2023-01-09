import pyttsx3
import speech_recognition as sr
import whatsapp



Assistant = pyttsx3.init("sapi5")
voices = Assistant.getProperty("voices")
# print(voices)
Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate', 170)


def Speak(Text):
    print("   ")
    Assistant.say(Text)
    print(f"Jarvis : {Text}")
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
    
def TaskHui():
    
    while True:
        
        query = takeCommand()
        # query = "whatsapp message to shreya"
        
        if 'hello' in query:
            Speak("Hello Sir , How are You ?")
        
        elif 'whatsapp message' in query:
            query = query.replace("jarvis","")
            query = query.replace("send","")
            query = query.replace("whatsapp message","")
            query = query.replace("to","")
            query = query.replace("my","")
            name = query
            print(name)
            if 'shreya' in name or 'girlfriend' in name or 'pallavi' in name :
                numb = "9142995706"
                Speak(f"What's The Message for {name}")
                mess = takeCommand()
                whatsapp.SendMessage(numb, mess)


TaskHui()