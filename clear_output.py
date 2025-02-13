# clear_output.py

import os
import platform

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Linux/MacOS
    else:
        _ = os.system('clear')

def close_proccess():
     # Close the terminal window based on the platform
    if platform.system() == 'Windows':
        os.system('taskkill /F /T /PID %i' % os.getpid())
    elif platform.system() in ['Linux', 'Darwin']:  # Linux or macOS
        os.system('kill -9 %i' % os.getpid())
    else:
        print("Unsupported operating system. Please close the terminal manually.")
