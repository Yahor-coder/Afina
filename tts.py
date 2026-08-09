from openai import OpenAI
from config import OPENAI_API_KEY
import pygame
import os

client = OpenAI(api_key=OPENAI_API_KEY)

pygame.mixer.init()


def speak(text):

    print("Афина:", text)

    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="nova",
        input=text
    )

    filename = "speech.mp3"

    response.write_to_file(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()

    os.remove(filename)