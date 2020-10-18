import pyttsx3
import pyjokes
import qrcode
import random
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
import pyautogui 
import cv2 
import numpy as np
from threading import Thread
import threading


    
def greetings():
    engine = pyttsx3.init()
    responses = [
        "Hi There! I am a play bot. Very nice to meet you.",
        "Wonderful, It is so nice to be in touch with you. I am a play bot.",
        "Warmest Welcome! I am a play bot.",
        "Having you here is really a great honour!",
        "I am very delighted to have you here. I am a play bot."
    ]
    s = random.choice(responses)+" Enter your number with '+Country_codeYour_number' Ex: +918332834979 without quotes :"
    engine.say(s)
    print(s)
    engine.runAndWait()
def comp_name(num):
    engine = pyttsx3.init()
    ph=phonenumbers.parse(num)
    s = "Hi "+geocoder.description_for_number(ph,'en')+"n! Are you a "+carrier.name_for_number(ph,'en')+" user. Ok then Let's play a Tic-Tac-Toe game."
    print(s)
    engine.say(s)
    engine.runAndWait()

def Recorder():
    resolution = (1920, 1080)  
    codec = cv2.VideoWriter_fourcc(*"XVID") 
    filename = "game_rec.avi"
    fps = 60.0
    out = cv2.VideoWriter(filename, codec, fps, resolution) 
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL) 
    cv2.resizeWindow("Live", 480, 270) 

    
    while True:
        img = pyautogui.screenshot() 
        frame = np.array(img)  
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
        out.write(frame) 
        cv2.imshow('Live', frame)
        if cv2.waitKey(1) == ord('q'): 
            break
    out.release() 
    cv2.destroyAllWindows()


def bot():
    greetings()
    num = input()
    comp_name(num)
    Thread(target=Recorder).start()
    import game
    Thread(target=game).start()



bot()
