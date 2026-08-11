import sounddevice as sd
import numpy as np
import webrtcvad
import wave
import time


SAMPLE_RATE = 16000
CHANNELS = 1

FRAME_DURATION = 30
FRAME_SIZE = int(SAMPLE_RATE * FRAME_DURATION / 1000)

SILENCE_DURATION = 1.2
MAX_RECORDING_TIME = 10

# Минимальная громкость, чтобы считать звук кандидатом на речь
VOLUME_THRESHOLD = 500


def record_audio(filename="record.wav"):

    vad = webrtcvad.Vad(1)

    frames = []

    started_speaking = False
    silence_start = None
    recording_start = time.time()

    print("🎤 Говорите...")

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16",
        blocksize=FRAME_SIZE
    ) as stream:

        while True:

            data, overflowed = stream.read(FRAME_SIZE)

            audio = data[:, 0]

            # Средняя громкость текущего блока
            volume = np.sqrt(np.mean(audio.astype(np.float32) ** 2))

            is_loud_enough = volume > VOLUME_THRESHOLD

            is_speech = False

            if is_loud_enough:
                try:
                    is_speech = vad.is_speech(
                        audio.tobytes(),
                        SAMPLE_RATE
                    )
                except Exception:
                    is_speech = False

            # --------------------------------
            # РЕЧЬ НАЧАЛАСЬ
            # --------------------------------

            if is_speech:

                started_speaking = True
                silence_start = None
                frames.append(audio.tobytes())

            # --------------------------------
            # ТИШИНА ПОСЛЕ РЕЧИ
            # --------------------------------

            elif started_speaking:

                frames.append(audio.tobytes())

                if silence_start is None:
                    silence_start = time.time()

                elif time.time() - silence_start >= SILENCE_DURATION:
                    break

            # --------------------------------
            # ЕЩЁ НИКТО НЕ ГОВОРИТ
            # --------------------------------

            else:

                # Не сохраняем фон вообще
                pass

            # Защита от бесконечной записи
            if time.time() - recording_start >= MAX_RECORDING_TIME:
                break

    # --------------------------------
    # РЕЧИ НЕ БЫЛО
    # --------------------------------

    if not started_speaking:

        print("🔇 Речь не обнаружена")

        return False

    # --------------------------------
    # СОХРАНЯЕМ WAV
    # --------------------------------

    audio_data = b"".join(frames)

    with wave.open(filename, "wb") as wav:

        wav.setnchannels(CHANNELS)
        wav.setsampwidth(2)
        wav.setframerate(SAMPLE_RATE)

        wav.writeframes(audio_data)

    print("✅ Запись завершена")

    return True