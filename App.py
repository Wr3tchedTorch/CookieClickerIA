from pyautogui import *
from threading import Thread
import threading
import pyautogui
import time
import keyboard
import win32api, win32con

pauseClick = False
appStatus = "idle"


def start_program():
    global appStatus
    
    print("Press S to start the program")
    
    while appStatus == "idle":
        if keyboard.is_pressed("s"): appStatus = "running"

def click(x, y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
def clickOnCookie():
    global appStatus
    global pauseClick
    
    try:
        cookiePos = pyautogui.locateOnScreen("./cookie.png", confidence=.8)
    except pyautogui.ImageNotFoundException:
        print("cookie image not found")
    
    while appStatus == "running":
        if (pauseClick):
            time.sleep(0.2)
            pauseClick = False
        click(cookiePos[0], cookiePos[1])        
        
def clickOnStore():
    global pauseClick
        
    t = threading.Timer(5, clickOnStore)
    t.daemon = True
    t.start()
    
    try:
        storePos = pyautogui.locateOnScreen("./legacy.png", grayscale=True, confidence=.7)        
        if (pyautogui.pixel(int(storePos[0]+124), int(storePos[1]+43))[0] > 200):
            pauseClick = True
            click(storePos[0]+124, storePos[1]+43)
    except pyautogui.ImageNotFoundException:
        print("store image not found")
    
def main():
    global appStatus
    global pauseClick
    
    isClicking = False
    offsetY = 20
    offsetX = 193    
    
    clickOnStore()
        
    while appStatus == "running":
        if (not isClicking):
            Thread(target=clickOnCookie).start()
            isClicking = True
        
        try:
            imagePos = pyautogui.locateOnScreen(image="./cursor.png", grayscale=True, confidence=0.8)
            
            if (pyautogui.pixel(int(imagePos[0])+offsetX, int(imagePos[1])+offsetY)[0] > 130):
                pauseClick = True
                pyautogui.click(x=int(imagePos[0])+offsetX, y=int(imagePos[1])+offsetY)
            
            offsetY += 67
            
            if (pyautogui.pixel(int(imagePos[0])+offsetX, int(imagePos[1])+offsetY)[0] < 50):
                offsetY = 20
                
        except pyautogui.ImageNotFoundException:
            print("Image not found")            
                
def exit_program():
    global appStatus
    
    print("Press Q to exit the program")
    
    while appStatus == "running":
        if keyboard.is_pressed('q') == True: appStatus = "idle"
        
start_program()
Thread(target=exit_program).start()
main()