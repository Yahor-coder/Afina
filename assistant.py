from chatgpt import ask_gpt, detect_command
from commands import *
from tts import speak

def local_command(text):

    text = text.lower().strip()

    # Убираем имя Афины из текста
    text = text.replace("афина", "")
    text = text.replace("афіна", "")
    text = text.strip(" ,.!?")

    # -------------------------
    # YOUTUBE
    # -------------------------

    youtube_words = [
        "youtube",
        "ютуб",
        "ютюб"
    ]

    if any(word in text for word in youtube_words):

        action_words = [
            "открой",
            "открыть",
            "запусти",
            "запустить",
            "покажи",
            "показать",
            "включи",
            "включить",
            "посмотреть",
            "смотреть",
            "зайди",
            "зайти",
            "хочу посмотреть"
        ]

        if any(action in text for action in action_words):
            return "OPEN_YOUTUBE"

    # -------------------------
    # EDGE / БРАУЗЕР
    # -------------------------

    browser_words = [
        "браузер",
        "edge",
        "эдж"
    ]

    if any(word in text for word in browser_words):

        action_words = [
            "открой",
            "открыть",
            "запусти",
            "запустить",
            "покажи",
            "показать",
            "зайди",
            "зайти"
        ]

        if any(action in text for action in action_words):
            return "OPEN_EDGE"

    # -------------------------
    # CALCULATOR / EXCEL
    # -------------------------

    calculator_words = [
        "калькулятор",
        "кальк",
        "excel",
        "эксель"
    ]

    if any(word in text for word in calculator_words):

        action_words = [
            "открой",
            "открыть",
            "запусти",
            "запустить",
            "покажи",
            "показать"
        ]

        if any(action in text for action in action_words):
            return "OPEN_CALC"

    # -------------------------
    # PROGRAMMING
    # -------------------------

    programming_words = [
        "visual studio",
        "visual studio code",
        "vscode",
        "pycharm",
        "arduino"
    ]

    if any(word in text for word in programming_words):

        action_words = [
            "открой",
            "открыть",
            "запусти",
            "запустить"
        ]

        if any(action in text for action in action_words):
            return "OPEN_NOTEPAD"

    # -------------------------
    # PAINT
    # -------------------------

    paint_words = [
        "paint",
        "пейнт"
    ]

    if any(word in text for word in paint_words):

        action_words = [
            "открой",
            "открыть",
            "запусти",
            "запустить",
            "покажи",
            "показать"
        ]

        if any(action in text for action in action_words):
            return "OPEN_PAINT"

    return None


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


def process_text(text):

    # Сначала пробуем БЕЗ GPT
    command = local_command(text)

    if command:
        print("LOCAL:", command)
        process_command(command)
        return command

    # Если локально не поняли — используем GPT
    command = detect_command(text)

    print("GPT:", command)

    if command == "CHAT":

        # -------------------------
        # GPT
        # -------------------------


        answer = ask_gpt(text)



        print("\nGPT")
        print()
        print("Афина:", answer)



        speak(answer)



        return "CHAT"

    process_command(command)

    return command