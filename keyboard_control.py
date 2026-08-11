import keyboard
import threading


stop_requested = False


def keyboard_listener():

    global stop_requested

    print("⌨️ F8 — остановить Афину")

    while True:

        keyboard.wait("f8")

        stop_requested = True


def start_keyboard_listener():

    thread = threading.Thread(
        target=keyboard_listener,
        daemon=True
    )

    thread.start()


def consume_stop_request():

    global stop_requested

    if stop_requested:

        stop_requested = False

        return True

    return False