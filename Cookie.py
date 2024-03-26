import pyautogui
import win32api, win32con
import sys, os
import time
from threading import Thread

class Cookie:
    appStatus = "running"
    scriptDir = sys.path[0]
    
    pauseClick = False
    cookiePos = [0, 0]
    
    buffStoreOffsetY = 20
    buffStoreOffsetX = 193
    
    def __init__(self):
        try:
            img_path = os.path.join(Cookie.scriptDir, 'images\cookie.png')
            self.cookiePos = pyautogui.locateOnScreen(img_path, confidence=.8)
        except pyautogui.ImageNotFoundException:
            print("cookie image not found")
    
    def click(self, x, y):
        win32api.SetCursorPos([x, y])
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.001)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
    def clickOnCookie(self):
        if (self.pauseClick):
            time.sleep(0.2)
            self.pauseClick = False
        self.click(self.cookiePos[0], self.cookiePos[1])
        
        Thread(target=self.clickOnCookie, daemon=True).start()
                
    def clickOnStore(self):
        try:
            img_path = os.path.join(self.scriptDir, 'images\legacy.png')
            storePos = pyautogui.locateOnScreen(img_path, grayscale=True, confidence=.7)
            if (pyautogui.pixel(int(storePos[0]+124), int(storePos[1]+43))[0] > 200):
                self.pauseClick = True
                self.click(int(storePos[0]+124), int(storePos[1]+43))
        except pyautogui.ImageNotFoundException:
            print("store image not found")
            
        time.sleep(5)
        Thread(target=self.clickOnStore, daemon=True).start()
    
    def buyNewBuff(self):
        try:
            img_path = os.path.join(self.scriptDir, 'images\cursor.png')
            imagePos = pyautogui.locateOnScreen(image=img_path, grayscale=True, confidence=0.8)
            
            if (pyautogui.pixel(int(imagePos[0])+self.buffStoreOffsetX, int(imagePos[1])+self.buffStoreOffsetY)[0] > 130):
                self.pauseClick = True
                pyautogui.click(x=int(imagePos[0])+self.buffStoreOffsetX, y=int(imagePos[1])+self.buffStoreOffsetY)
            
            self.buffStoreOffsetY += 67
            
            if (pyautogui.pixel(int(imagePos[0])+self.buffStoreOffsetX, int(imagePos[1])+self.buffStoreOffsetY)[0] < 50):
                self.buffStoreOffsetY = 20
                
        except pyautogui.ImageNotFoundException:
            print("Image not found")
            
        self.buyNewBuff()