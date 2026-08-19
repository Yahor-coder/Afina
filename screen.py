from PIL import ImageGrab


def take_screenshot():
    print("🖥️ Делаю скриншот экрана...")

    screenshot = ImageGrab.grab()

    return screenshot