from pyautogui import *
from threading import Thread
import keyboard
from Cookie import Cookie

pauseClick = False
appStatus = "idle"

def start_program():
    global appStatus
    
    print("Press S to start the program")
    
    while appStatus == "idle":
        if keyboard.is_pressed("s"): appStatus = "running"
    
def main():
    global appStatus
    
    cookieClicker = Cookie()
    
    Thread(target=cookieClicker.clickOnStore, daemon=True).start()        
    Thread(target=cookieClicker.clickOnCookie, daemon=True).start()    
    Thread(target=cookieClicker.buyNewBuff, daemon=True).start()
    
    exit_program()
                
def exit_program():
    global appStatus
    
    print("Press Q to exit the program")
    
    while appStatus == "running":
        if keyboard.is_pressed('q') == True: 
            exit(0)
        
start_program()
main()