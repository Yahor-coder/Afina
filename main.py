import keyboard

from recorder import record_audio
from chatgpt import speech_to_text
from assistant import process_text
from tts import speak

def is_afina(text):
    text = text.lower().strip()

    variants = [
        "афина",
        "афіна",
        "атина",
        "athena",
        "αθήνα",
        "αθηνα",
        "афине",
        "афиной",
        "афину",
        "Athina"
    ]

    return any(word in text for word in variants)
def listen(filename="record.wav"):

    print("🎤 Говорите...")

    spoken = record_audio(filename)

    if not spoken:
        return ""

    text = speech_to_text(filename)

    print("\n==========")
    print(text)
    print("==========\n")

    return text


print("================================")
print("        АФИНА")
print("================================")
print("🔴 Афина выключена")
print("Нажмите F10 для активации")
print("================================")


while True:

    keyboard.wait("f10")

    print("\n🟢 F10 нажата")
    print("🎤 Скажите «Афина»")

    text = listen()

    if not is_afina(text):
        print("❌ Слово «Афина» не найдено")
        print("🔴 Афина остаётся выключенной")
        continue

    speak("Здравствуйте, чем могу помочь?")

    print("🟢 Афина активна")

    while True:

        text = listen()

        if not text:
            continue

        lower_text = text.lower()

        # Выключение Афины
        if "спасибо" in lower_text and "афин" in lower_text:
            speak("Хорошо. До свидания.")
            print("🔴 Афина выключена")
            break

        # Обычная команда / вопрос
        process_text(text)