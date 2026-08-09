import sounddevice as sd
import soundfile as sf


def record_audio(filename, duration=5, samplerate=16000):

    print("🎤 Говорите...")

    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    sf.write(
        filename,
        audio,
        samplerate
    )

    print("✅ Запись завершена")