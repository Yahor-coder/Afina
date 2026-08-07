from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def detect_command(text):
    prompt = f"""
    Ты являешься маршрутизатором команд голосового помощника Афина.

    Тебе необходимо определить, какую команду хотел выполнить пользователь.

    Доступные команды:

    OPEN_EDGE
    — открыть браузер Edge
    — открыть Telegram
    — открыть интернет
    — открыть браузер

    OPEN_CALC
    — открыть калькулятор
    — открыть финансовые таблицы
    — открыть Excel

    OPEN_NOTEPAD
    — открыть Arduino IDE
    — открыть PyCharm
    — открыть Visual Studio
    — открыть Visual Studio Code
    — открыть среду разработки
    — начать программирование

    OPEN_PAINT
    — открыть Paint
    — открыть редактор рисунков

    OPEN_YOUTUBE
    — открыть YouTube
    — открыть видео

    Если запрос относится к одной из этих команд —
    ответь ТОЛЬКО названием команды.

    Если пользователь задаёт вопрос или просто разговаривает —
    ответь только:

    CHAT

    Запрос пользователя:

    {text}
    """

    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )

    return response.output_text.strip()


def ask_gpt(question):

    response = client.responses.create(
        model="gpt-5.5",
        input=question
    )

    return response.output_text.strip()
def speech_to_text(filename):

    with open(filename, "rb") as audio_file:

        transcript = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=audio_file
        )

    return transcript.text