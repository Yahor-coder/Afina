from assistant import process_text

print("===================================")
print("Afina Text Mode")
print("Введите сообщение.")
print("Для выхода напишите: exit")
print("===================================")

while True:

    text = input("\nВы: ")

    if text.lower() == "exit":
        break

    process_text(text)