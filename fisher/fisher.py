from time import sleep
from winops import winops
import pyautogui
from threading import Timer
import threading
from consumer.data import openInvKey
from consumer.consumer import startConsumer, pixelChecker, eatPixel, eatPixelRGB, drinkPixel, drinkPixelRGB, useFishingRod, winSendKey, isMenuOpen


hungerStatus = False
thirstStatus = False
class ThreadTimer():
    _instance = None
    _lock = threading.Lock() 

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls.isBusy = False
                    cls.theThread = Timer(5,useFishingRod, [cls])
                    cls._instance = super(ThreadTimer, cls).__new__(cls)
        return cls._instance

    def rodUsage(cls):
        cls.setBusy(cls)
        useFishingRod()
        cls.setNotBusy(cls)

    def setBusy(cls):
        cls.isBusy = True

    def setNotBusy(cls):
        cls.isBusy = False

    def start(cls):
        cls.theThread.start()

    def cancel(cls):
        cls.theThread.cancel()

t = ThreadTimer()

def afkMode(window, letter, afkVar):
    if afkVar == True:
        hungerStatus = pixelChecker(eatPixel, eatPixelRGB)
        thirstStatus = pixelChecker(drinkPixel, drinkPixelRGB)
        if hungerStatus or thirstStatus:
            winops.focusWindow(window)
            startConsumer(t)
            sleep(1)
        winops.focusWindow(window)
        winops.sendkey(window, letter)
    else:
        winops.sendkey(window, letter)


def startFishing(winVar, afkVar):
    if afkVar:
        winops.focusWindow(winVar)
        if not t.isBusy:
            try:
                t.start()
            except:
                pass
        else:
            try:
                t.cancel()
            except:
                pass

    mainBarPixelColorGreen = (60,150,60)
    mainBarPixel = pyautogui.pixel(950, 107)
    if  mainBarPixel == mainBarPixelColorGreen:
        if afkVar:
            if t:
                t.cancel() 
        gPixel1 = pyautogui.pixel(900, 147)
        gColor1 = (114, 204, 114)
        gPixel2 = pyautogui.pixel(900, 153)
        gColor2 = (114, 204, 114)

        eBotPixel = pyautogui.pixel(896, 153)
        eBotColor = (114, 204, 114)

        wPixel1 = pyautogui.pixel(892, 146)
        wColor1 = (114, 204, 114)
        wPixel2 = pyautogui.pixel(887, 145)
        wColor2 = (113, 202, 113)

        sPixel1 = pyautogui.pixel(895, 140)
        sColor1 = (114, 204, 114)
        sPixel3 = pyautogui.pixel(892, 146)
        sColor3 = (114, 204, 114)

        fPixel1 = pyautogui.pixel(891, 145)
        fPixel2 = pyautogui.pixel(893, 154)

        if gPixel1 == gColor1 and gPixel2 == gColor2:
            afkMode(winVar, 'g', afkVar)
        elif eBotPixel == eBotColor:
            afkMode(winVar, 'e', afkVar)
        elif wPixel1 == wColor1 and wPixel2 == wColor2:
            afkMode(winVar, 'w', afkVar)
        elif sPixel1 == sColor1 and sPixel3 == sColor3:
            afkMode(winVar, 's', afkVar)
        elif fPixel1 == (114, 204, 114) and fPixel2 != (114, 204, 114):
            afkMode(winVar, 'f', afkVar)