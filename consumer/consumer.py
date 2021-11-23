import cv2
import time
from numpy import true_divide
import pytesseract
import pyautogui
from consumer.data import *
from pywinauto.application import Application

app = Application().connect(title_re="FiveM")
win = app.window(title_re = "FiveM")

isHungry = False
isThirsty = False


def isMenuOpen():
    useText='USE'
    pyautogui.screenshot(region=(UseButtomRegion)).save(r'img\usebutton.png')
    img = cv2.imread(r'img\usebutton.png')
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    custom = '--psm 6 --oem 3 -c tessedit_char_whitelist=QWERTYUIOPASDFGHJKLZXCVBNM-'
    txt = pytesseract.image_to_string(img, config=custom, lang='eng')
    time.sleep(1)

    if useText == txt[:-1]:
        return True
    else:
        return False
        

def useFishingRod():
    #open f2 menu
    winSendKey(win, openInvKey)
    #wait
    time.sleep(2)
    #is f2 menu open?
    menuStatus = isMenuOpen()

    if not menuStatus:
        winSendKey(win, openInvKey)
        time.sleep(2)

    squareObjects = [Square() for i in range(len(textBoxRegions))]

    #find square that has fishing rod
    for i in range(len(textBoxRegions)):
        #set the textbox region equivalent to the position in the textBoxRegions array list
        squareObjects[i].textBoxRegion = textBoxRegions[i]
        #set cursor position for item
        squareObjects[i].itemLoc = [(textBoxRegions[i][0] + 57), (textBoxRegions[i][1] - 30)]
        #set text for square.textBoxContent
        tbr = squareObjects[i].textBoxRegion
        screenFunc(tbr, squareObjects[i])

    #begin operation
    for i in range(len(squareObjects)):
        if fishingRodText in squareObjects[i].textBoxContent:
            consume(squareObjects[i].itemLoc)





def winSendKey(window, letter):
    window.send_keystrokes(letter)

def pixelChecker(actionPixelLoc, actionPixelColor):
    # meinPixel = pyautogui.pixel(actionPixelLoc[0], actionPixelLoc[1])
    meinPixel = pyautogui.pixelMatchesColor(actionPixelLoc[0], actionPixelLoc[1], (actionPixelColor), tolerance = 30)
    if meinPixel:
        return False
    else:
        return True

def consume(itemLoc):
    pyautogui.moveTo(itemLoc)   # moves mouse to X of 100, Y of 200.
    time.sleep(1)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.moveTo(useButtonLoc)   # moves mouse to X of 100, Y of 200.
    time.sleep(1)
    pyautogui.mouseUp(button='left')

def screenFunc(aList, squareObj = {}):
    pyautogui.screenshot(region=(aList)).save(r'img\titties.png')
    img = cv2.imread(r'img\titties.png')
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    custom = '--psm 6 --oem 3 -c tessedit_char_whitelist=QWERTYUIOPASDFGHJKLZXCVBNM-'
    txt = pytesseract.image_to_string(img, config=custom, lang='eng')

    if squareObj:
        squareObj.textBoxContent = txt[:-1]
    return txt


def startConsumer():
    consumables = Consumables()
    squareObjects = [Square() for i in range(len(textBoxRegions))]
    isHungry = pixelChecker(eatPixel, eatPixelRGB)
    isThirsty = pixelChecker(drinkPixel, drinkPixelRGB)

    for i in range(len(textBoxRegions)):
        #set the textbox region equivalent to the position in the textBoxRegions array list
        squareObjects[i].textBoxRegion = textBoxRegions[i]
        #set cursor position for item
        squareObjects[i].itemLoc = [(textBoxRegions[i][0] + 57), (textBoxRegions[i][1] - 30)]
        #set text for square.textBoxContent
        tbr = squareObjects[i].textBoxRegion
        loopText = screenFunc(tbr, squareObjects[i])

    while isHungry or isThirsty:
            if isHungry:
                #hit F2
                winSendKey(win, openInvKey)
                #wait
                time.sleep(2)
                #Check that menu is open

                #begin operation
                for i in range(len(squareObjects)):
                    for item in consumables.foodList:
                        if item in squareObjects[i].textBoxContent:
                            isHungry = pixelChecker(eatPixel, eatPixelRGB)
                            consume(squareObjects[i].itemLoc)
                            isHungry = pixelChecker(eatPixel, eatPixelRGB)
            elif isThirsty:
                for i in range(len(squareObjects)):
                    for item in consumables.drinkList:
                        if item in squareObjects[i].textBoxContent:
                            isThirsty = pixelChecker(drinkPixel, drinkPixelRGB)
                            consume(squareObjects[i].itemLoc)
                            isThirsty = pixelChecker(drinkPixel, drinkPixelRGB)
            else:
                print('We are fine')
                isThirsty = pixelChecker(eatPixel, eatPixelRGB)

