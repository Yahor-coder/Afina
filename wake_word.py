import openwakeword
from openwakeword.model import Model

import sounddevice as sd
import numpy as np


print("Загрузка wake-word моделей...")

openwakeword.utils.download_models()

model = Model(
    wakeword_models=["hey_jarvis"]
)

print("Готово.")
print("🎤 Слушаю локально...")
print("Скажи: Hey Jarvis")


def audio_callback(indata, frames, time, status):

    audio = (indata[:, 0] * 32767).astype(np.int16)

    prediction = model.predict(audio)

    for name, score in prediction.items():

        if score > 0.5:

            print(f"🔥 {name}: {score:.2f}")


with sd.InputStream(
    samplerate=16000,
    channels=1,
    dtype="float32",
    blocksize=1280,
    callback=audio_callback
):

    while True:

        sd.sleep(1000)