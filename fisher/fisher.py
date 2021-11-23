from winops import winops
import pyautogui
from threading import Timer
from consumer.consumer import useFishingRod



def startFishing(winVar, afkVar):
        print('beforeTimer')
        theTimer = Timer(5.0,useFishingRod(),[])
        print('timerStarted')
        theTimer.start()
        mainBarPixelColorGreen = (60,150,60)
        mainBarPixel = pyautogui.pixel(950, 107)
        if  mainBarPixel == mainBarPixelColorGreen:
            theTimer.cancel()
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
                winops.isAfk(winVar, 'g', afkVar)
            elif eBotPixel == eBotColor:
                winops.isAfk(winVar, 'e', afkVar)
            elif wPixel1 == wColor1 and wPixel2 == wColor2:
                winops.isAfk(winVar, 'w', afkVar)
            elif sPixel1 == sColor1 and sPixel3 == sColor3:
                winops.isAfk(winVar, 's', afkVar)
            elif fPixel1 == (114, 204, 114) and fPixel2 != (114, 204, 114):
                winops.isAfk(winVar, 'f', afkVar)