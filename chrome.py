import os

def close_chrome():
    # Checking for the operating system
    platform = os.name

    # Command for Windows
    if platform == 'nt':
        os.system("taskkill /im chrome.exe /f")

    # Command for MacOS
    elif platform == 'posix':
        os.system("pkill -f 'Google Chrome'")

    # Command for Linux
    else:
        os.system("pkill chrome")


