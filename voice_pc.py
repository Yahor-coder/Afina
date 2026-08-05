import serial
import serial.tools.list_ports
import subprocess
import webbrowser
import time


def connect():

    while True:

        ports = serial.tools.list_ports.comports()

        if len(ports) == 0:

            print("Waiting for Arduino...")
            time.sleep(2)
            continue

        try:

            port = ports[0]

            ser = serial.Serial(port.device, 115200, timeout=1)

            print(f"Connected to {port.device} ({port.description})")

            return ser

        except Exception as e:

            print(e)

            time.sleep(2)


ser = connect()

# Даём Arduino полностью загрузиться после открытия COM-порта
time.sleep(2)

print("Voice assistant started")
print("Waiting for commands...")


while True:

    try:

        line = ser.readline().decode(errors="ignore").strip()

    except Exception:

        print("Connection lost")

        try:
            ser.close()
        except Exception:
            pass

        ser = connect()

        # После переподключения снова ждём загрузку Arduino
        time.sleep(2)

        continue

    if not line:
        continue

    print("Received:", line)

    # ------------------------------
    # БРАУЗЕР + TELEGRAM
    # ------------------------------

    if line == "OPEN_EDGE":

        subprocess.Popen([
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        ])

        subprocess.Popen(
            r"D:\Telegram Desktop\Telegram.exe"
        )

    # ------------------------------
    # ДЕНЬГИ
    # ------------------------------

    elif line == "OPEN_CALC":

        subprocess.Popen("calc.exe")

        subprocess.Popen([
            "explorer",
            r"C:\Users\Goodf\Desktop\таблицы деньги\Личный бюджет 2025.xlsx"
        ])

        subprocess.Popen([
            "explorer",
            r"C:\Users\Goodf\Desktop\таблицы деньги\Таблица для всех инвестиции (учёт вложений).xlsx"
        ])

    # ------------------------------
    # ПРОГРАММИРОВАНИЕ
    # ------------------------------

    elif line == "OPEN_NOTEPAD":

        subprocess.Popen(
            r"C:\Users\Goodf\AppData\Local\Programs\Arduino IDE\Arduino IDE.exe"
        )

        subprocess.Popen(
            r"D:\PyCharm Community Edition 2025.2.6\bin\pycharm64.exe"
        )

        subprocess.Popen(
            r"C:\Program Files\Microsoft Visual Studio\18\Enterprise\Common7\IDE\devenv.exe"
        )

    # ------------------------------
    # PAINT
    # ------------------------------

    elif line == "OPEN_PAINT":

        subprocess.Popen("mspaint.exe")

    # ------------------------------
    # CHATGPT
    # ------------------------------

    elif line == "OPEN_CHATGPT":

        webbrowser.open("https://chatgpt.com")

    # ------------------------------
    # YOUTUBE
    # ------------------------------

    elif line == "OPEN_YOUTUBE":

        webbrowser.open("https://youtube.com")