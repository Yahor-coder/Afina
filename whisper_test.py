from recorder import record_audio
from assistant import process_text
from chatgpt import speech_to_text
from tts import speak


active = False


def is_wake_word(text):

    text = text.lower().strip()

    wake_words = [
        "афина",
        "афіна",
        "αθήνα",
        "athena"
    ]

    return any(word in text for word in wake_words)


def remove_wake_word(text):

    text = text.lower().strip()

    wake_words = [
        "афина",
        "афіна",
        "αθήνα",
        "athena"
    ]

    for word in wake_words:

        text = text.replace(word, "")

    return text.strip()


while True:

    try:

        # =====================================
        # WAITING
        # =====================================

        if not active:

            print("\n🎤 Жду слово «Афина»...")

            record_audio("record.wav")

            text = speech_to_text("record.wav").strip()

            if not text:
                continue

            print("\n==========")
            print(text)
            print("==========")

            # Проверяем wake word
            if not is_wake_word(text):

                print("Игнорирую.")

                continue

            # Убираем "Афина"
            command_text = remove_wake_word(text)

            # -----------------------------
            # Только "Афина"
            # -----------------------------

            if not command_text:

                speak("Да?")

                active = True

                continue

            # -----------------------------
            # "Афина, открой YouTube"
            # -----------------------------

            print("Команда после активации:", command_text)

            process_text(command_text)

            continue


        # =====================================
        # ACTIVE
        # =====================================

        print("\n🎤 Слушаю команду...")

        record_audio("record.wav")

        text = speech_to_text("record.wav").strip()

        if not text:
            continue

        print("\n==========")
        print(text)
        print("==========")

        process_text(text)

        active = False


    except KeyboardInterrupt:

        print("\nАфина остановлена.")

        break


    except Exception as e:

        print("\nОшибка:", e)

        active = False