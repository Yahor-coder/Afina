from microphone import record_audio
from assistant import process_text
from chatgpt import speech_to_text

record_audio()

text = speech_to_text("voice.wav")

print("\nВы сказали:", text)

process_text(text)