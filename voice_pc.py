import serial
import serial.tools.list_ports
import time
from assistant import process_command

def send_ok():
    ser.write(b"PC:OK\n")

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

    try:
        process_command(line)  # эта функция уже из assistant.py
        send_ok()

    except Exception as e:
        print(e)
        ser.write(b"PC:ERROR\n")