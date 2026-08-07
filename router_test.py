from chatgpt import detect_command

while True:

    text = input(">>> ")

    print(detect_command(text))