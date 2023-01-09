import webbrowser as web
import time
import keyboard


def SendMessage(number, message):
    
    number = '+91'+ number
    open_chat = "https://web.whatsapp.com/send?phone="+ number + "&text=" + message
    web.open(open_chat)
    time.sleep(15)
    keyboard.press('enter')
    
def whatsApp_grp(group_id, message):
    open_chat = "https://web.whatsapp.com/accept?code="+ group_id
    web.open(open_chat)
    keyboard.write(message)
    time.sleep(1)
    keyboard.press('enter')   

