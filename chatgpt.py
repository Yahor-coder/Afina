from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def detect_command(text):

    prompt = f"""
Ты являешься маршрутизатором команд голосового помощника Афина.

Доступные команды:

STOP_SPEAKING
— Афина, замолчи
— замолчи
— прекрати говорить
— хватит говорить

DEACTIVATE_ASSISTANT
— спасибо Афина
— спасибо, Афина
— Афина, выключись
— выключись
— пока Афина

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


conversation = []


def ask_gpt(question):

    global conversation

    # Добавляем вопрос пользователя
    conversation.append({
        "role": "user",
        "content": question
    })

    # Ограничиваем память последними 10 сообщениями,
    # чтобы история не разрасталась бесконечно
    conversation = conversation[-10:]

    response = client.responses.create(
        model="gpt-5.5",
        input=[
            {
                "role": "system",
                "content": """
Ты — голосовой помощник Афина.

Ты разговариваешь с пользователем голосом.

Правила:
- отвечай естественно и кратко;
- обычно 2–4 предложения;
- максимум около 80 слов;
- без Markdown;
- без заголовков;
- без списков, если они не нужны;
- без эмодзи;
- отвечай на русском языке, если пользователь говорит по-русски;
- учитывай предыдущие сообщения в текущем разговоре;
- если пользователь говорит "он", "она", "это", "там", "тогда" и т.п.,
  используй контекст предыдущих сообщений;
- не повторяй вопрос пользователя;
- сразу отвечай по существу.

Если пользователь просит подробно объяснить тему,
можешь дать более длинный ответ.
"""
            }
        ] + conversation
    )

    answer = response.output_text.strip()

    # Сохраняем ответ Афины в историю
    conversation.append({
        "role": "assistant",
        "content": answer
    })

    # Оставляем последние 10 сообщений
    conversation = conversation[-10:]

    return answer
def speech_to_text(filename):

    with open(filename, "rb") as audio_file:

        transcript = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=audio_file,
            language="ru"
        )

    return transcript.text