from translator import translate
from chat import chatbot
from text2speech import text2speech

from speech2text import speech2text

import pyaudio
import pyttsx3
# import speech_recognition as sr 
import time
import struct
import pvporcupine
import pygame


USER = "Nobita"

def playSound(filename):
    pygame.init()

    # Load the audio file
    
    pygame.mixer.music.load(filename)

    # Play the audio file
    pygame.mixer.music.play()

    # Wait for the audio to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()
    pygame.quit()






def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # change number to change voces 
    # the voice inside the window 
    engine.setProperty('voice', voices[1].id)
    print("J.A.V.I.S.: " + text + "\n")
    engine.say(text)
    engine.runAndWait()

# speak("Hello, what are you doing")


def vibot():
    while True:
        # user_input = input("Nobita: ")
        
        user_input = speech2text()
        

        yousaid = translate(user_input, 'vi_en')
        if(yousaid == "" or yousaid.lower == "goodbye"):
            # text2speech("Bái bai!!")
            playSound("sounds/baibaia.mp3")
            break
        
        
        botrep = chatbot(yousaid)
        botsaid = translate(botrep, 'en_vi')
        print("Doraemon: " + botsaid)
        
        text2speech(botsaid)
        

# vibot()


def main():
    porcupine = None 
    pa = None
    audio_stream = None 

    print("J.A.V.I.S. version 1.2 - Online and Ready!!")
    print("*******************************************")
    print("J.A.V.I.S. Awaiting your call!! " + USER)

    try:
        porcupine = pvporcupine.create(keywords = ["jarvis", "computer"])
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(rate = porcupine.sample_rate,
         channels = 1,
          format = pyaudio.paInt16, 
          input=True,frames_per_buffer=porcupine.frame_length)

        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0: ###the fun game happen here
                print("Hotword Detected .. ", end="")
                playSound("sounds/listening.mp3")

                playSound('sounds/daemday.mp3')
                # speak("I'm here sir")
                # time.sleep(1)
                print("J.A.R.V.I.S..: Awaiting your call " + USER)
                vibot() 
    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if pa is not None:
            pa.terminate()


    
main()        










