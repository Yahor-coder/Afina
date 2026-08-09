from recorder import record_audio
from assistant import process_text
from chatgpt import speech_to_text

while True:

    try:
        print("\n🎤 Говорите...")

        record_audio("record.wav")

        print("✅ Запись завершена")

        text = speech_to_text("record.wav")

        if not text.strip():
            continue

        print("\n==========")
        print(text)
        print("==========\n")

        process_text(text)

    except KeyboardInterrupt:
        print("\nАфина остановлена.")
        break

    except Exception as e:
        print("Ошибка:", e)
        print("Перезапуск прослушивания...")