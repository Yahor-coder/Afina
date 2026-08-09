from chatgpt import ask_gpt, detect_command
from commands import *
from tts import speak


def process_command(command):

    if command == "OPEN_EDGE":
        open_edge()

    elif command == "OPEN_CALC":
        open_calc()

    elif command == "OPEN_NOTEPAD":
        open_programming()

    elif command == "OPEN_PAINT":
        open_paint()

    elif command == "OPEN_YOUTUBE":
        open_youtube()

    else:
        print("Неизвестная команда:", command)


def process_text(text):

    text = text.strip()

    command = detect_command(text)

    print("GPT:", command)

    if command == "CHAT":

        answer = ask_gpt(text)

        print("\n========== GPT ==========")
        print(answer)
        print("=========================\n")

        speak(answer)

        return

    process_command(command)