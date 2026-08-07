import subprocess
import webbrowser


def open_edge():
    subprocess.Popen([
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    ])

    subprocess.Popen(
        r"D:\Telegram Desktop\Telegram.exe"
    )


def open_calc():
    subprocess.Popen("calc.exe")

    subprocess.Popen([
        "explorer",
        r"C:\Users\Goodf\Desktop\таблицы деньги\Личный бюджет 2025.xlsx"
    ])

    subprocess.Popen([
        "explorer",
        r"C:\Users\Goodf\Desktop\таблицы деньги\Таблица для всех инвестиции (учёт вложений).xlsx"
    ])


def open_programming():

    subprocess.Popen(
        r"C:\Users\Goodf\AppData\Local\Programs\Arduino IDE\Arduino IDE.exe"
    )

    subprocess.Popen(
        r"D:\PyCharm Community Edition 2025.2.6\bin\pycharm64.exe"
    )

    subprocess.Popen(
        r"C:\Program Files\Microsoft Visual Studio\18\Enterprise\Common7\IDE\devenv.exe"
    )


def open_paint():
    subprocess.Popen("mspaint.exe")


def open_youtube():
    webbrowser.open("https://youtube.com")