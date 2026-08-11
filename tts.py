from openai import OpenAI
from config import OPENAI_API_KEY
import pygame
import os
from keyboard_control import start_keyboard_listener, consume_stop_request


client = OpenAI(api_key=OPENAI_API_KEY)

pygame.mixer.init()

start_keyboard_listener()


def speak(text):

    print("Афина:", text)

    # =========================
    # TTS — генерация аудио
    # =========================


    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="nova",
        input=text
    )

    filename = "speech.mp3"

    response.write_to_file(filename)




    # =========================
    # Воспроизведение
    # =========================


    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    interrupted = False

    while pygame.mixer.music.get_busy():

        if consume_stop_request():

            print("🔇 Афина остановлена")

            pygame.mixer.music.stop()

            interrupted = True

            break

        pygame.time.Clock().tick(20)



    pygame.mixer.music.unload()

    if os.path.exists(filename):
        os.remove(filename)

    return not interrupted