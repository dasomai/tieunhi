import pyaudio
import os
import time
import pyaudio
import wave
import pygame

def playSound(filename):
    pygame.init()

    # Load the audio file
    
    pygame.mixer.music.load(filename)

    # Play the audio file
    pygame.mixer.music.play()

    # Wait for the audio to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)




def speech2text():
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 3
    filename = "output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')
    playSound("listening.mp3")

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()


    playSound("done.mp3")

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()


    from os import path
    from pydub import AudioSegment

    # Enter the filename you want to convert it should in the same folder as this python file
    src = "output.wav"
    dst = "output.mp3"

    #convert wav to mp3
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

    print("Converted Successfully")


    from google.cloud import speech
    client = speech. SpeechClient . from_service_account_file ('key.json')
    file_name = "output.mp3"
    with open (file_name, 'rb') as f:
        mp3_data = f.read()


    audio_file = speech.RecognitionAudio(content=mp3_data)
    config = speech.RecognitionConfig(
        sample_rate_hertz=44100,
        enable_automatic_punctuation=True,
        # language_code='en-US',
        language_code='Vi',

        audio_channel_count=2
    )

    response = client.recognize(
        config=config,
        audio=audio_file
    )

    # print(response)
    text = ""

    for result in response.results:
        print(result.alternatives[0].transcript)
        text = result.alternatives[0].transcript

    return text

    




