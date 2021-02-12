import time

def countdown(zeit, sekunden_warten=1):
    while zeit > 0:
        print(zeit)
        zeit -= 1
        time.sleep(sekunden_warten)
    print("Ende!")

countdown(10)