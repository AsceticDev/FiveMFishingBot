from pywinauto import win32defines 
from consumer.consumer import pixelChecker, eatPixelRGB, eatPixel, drinkPixelRGB, drinkPixel, startConsumer


def sendkey(window, letter):
    window.send_keystrokes(letter)
    print(letter)

def isAfk(window, letter, afkVar):
    if afkVar == True:
        hungerStatus = pixelChecker(eatPixel, eatPixelRGB)
        thirstStatus = pixelChecker(drinkPixel, drinkPixelRGB)
        if hungerStatus or thirstStatus:
            startConsumer()
        else:
            setFocus(window, letter)
    else:
        sendkey(window, letter)

def setFocus(window, letter):
    if window.has_style(win32defines.WA_INACTIVE): # if minimized
        window.set_focus()
        sendkey(window, letter)
    else:
        sendkey(window, letter)