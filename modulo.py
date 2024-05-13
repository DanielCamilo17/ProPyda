from colorama import init, Fore, Style
import time

def colortexto(text):
    for chart in text:
        print(Fore.RED + chart, end="",flush=True)
        time.sleep(0.001)
    # print(Style.reset_all)
    


