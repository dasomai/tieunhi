from gtts import gTTS
import os
import pygame


def text2speech(text):
   
    message = text

    tts = gTTS(message, lang='vi')
    

    # os.chmod("message.mp3", 0o666)
    # Save the audio file
    tts.save("message.mp3")

    # Initialize pygame
    pygame.init()

    # Load the audio file
    audio_file = "message.mp3"
    pygame.mixer.music.load(audio_file)

    # Play the audio file
    pygame.mixer.music.play()

    # Wait for the audio to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.stop()
    pygame.quit()
